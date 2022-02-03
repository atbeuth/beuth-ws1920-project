from datetime import datetime

from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.views.generic import DetailView
from imageposts.models import Imagepost

from .forms import InstagramProfileForm, ProfileForm, UserForm
from .models import Follower, InstagramProfile, Profile
from .scraper import InstagramImageScraper


# Create your views here.
def profile(request):
    return render(request, "user/profile.html")


# DetailViews
class UserDetailView(DetailView):
    model = User
    template_name = "user/profile.html"
    context_object_name = "user_p"

    def post(self, request, *args, **kwargs):
        username_to_toggle = request.POST.get("username").strip()

        users = User.objects.all()
        user = None

        for current_user in users:
            if current_user.username == username_to_toggle:
                user = current_user

        Profile.objects.toggle_follow(user, request.user, username_to_toggle)
        return HttpResponseRedirect(request.POST.get("url").strip())

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context["user_list"] = User.objects.all()
        context["imagepost_list"] = Imagepost.objects.all()

        user = context["user_p"]
        is_Following = False
        if self.request.user.is_authenticated:
            if user.profile in self.request.user.is_following.all():
                is_Following = True
            context["is_following"] = is_Following

        return context


class UserBioView(DetailView):
    model = User
    template_name = "user/bio.html"
    context_object_name = "user_p"


class UserImagesView(DetailView):
    model = User
    template_name = "user/profile_images.html"
    context_object_name = "user_p"

    def post(self, request, *args, **kwargs):
        username_to_toggle = request.POST.get("username").strip()

        users = User.objects.all()
        user = None

        for current_user in users:
            if current_user.username == username_to_toggle:
                user = current_user

        Profile.objects.toggle_follow(user, request.user, username_to_toggle)
        return HttpResponseRedirect(request.POST.get("url").strip())

    def get_context_data(self, **kwargs):
        context = super(UserImagesView, self).get_context_data(**kwargs)
        context["user_list"] = User.objects.all()
        context["imagepost_list"] = Imagepost.objects.all()

        user = context["user_p"]
        is_Following = False
        if self.request.user.is_authenticated:
            if user.profile in self.request.user.is_following.all():
                is_Following = True
            context["is_following"] = is_Following

        return context


# ListViews
class FollowerView(DetailView):
    model = User
    template_name = "user/profile_follows.html"
    context_object_name = "user_p"

    def post(self, request, *args, **kwargs):
        username_to_toggle = request.POST.get("username").strip()

        users = User.objects.all()
        user = None

        for current_user in users:
            if current_user.username == username_to_toggle:
                user = current_user

        Profile.objects.toggle_follow(user, request.user, username_to_toggle)
        return HttpResponseRedirect(request.POST.get("url").strip())

    def get_context_data(self, **kwargs):
        context = super(FollowerView, self).get_context_data(**kwargs)
        context["follower_list"] = Follower.objects.all()

        user = context["user_p"]
        is_Following = False
        if self.request.user.is_authenticated:
            if user.profile in self.request.user.is_following.all():
                is_Following = True
            context["is_following"] = is_Following

        return context


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = "/user/login/?sgu_alert=1"
    template_name = "registration/signup.html"


def user_edit(request):
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("/user/settings/", pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, "user/user_settings.html", {"form": form})


def profile_edit(request):
    profile = get_object_or_404(Profile, pk=request.user.id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect("/user/profile/settings/", pk=profile.pk, user=profile.user)
    else:
        form = ProfileForm(instance=profile)
    return render(request, "user/profile_settings.html", {"form": form})


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("/user/profile/settings/")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "user/change_password.html", {"form": form})


# ----------------
#   instagram
# ----------------


def get_instagram_data(username):
    scraper = InstagramImageScraper()
    data = scraper.get_dict(username)
    return [data["profile"]["profilPicturePath"], data["media"]]


def add_insta_profile(request):
    insta_profile = get_object_or_404(
        InstagramProfile, pk=request.user.instagramprofile.id
    )
    if request.method == "POST":
        form = InstagramProfileForm(request.POST, request.FILES, instance=insta_profile)
        if form.is_valid():
            insta_profile = form.save(commit=False)

            data = get_instagram_data(form.cleaned_data["instagram_username"])
            insta_profile.instagram_profile_img_url = data[0]
            insta_profile.instagram_posts = data[1]
            insta_profile.date_scraped = datetime.today().strftime("%Y-%m-%d")

            insta_profile.save()
            return redirect("/user/{}/images".format(request.user.id))
    else:
        form = InstagramProfileForm(instance=insta_profile)
    return render(request, "instagram/instagram_form.html", {"form": form})


def show_insta_profile(request, pk):
    return render(
        request,
        "instagram/instagram.html",
        {"pk": pk, "insta_profile": request.user.instagramprofile},
    )
