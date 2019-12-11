from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from django.views.generic import DetailView, ListView, UpdateView, FormView, View
from django.contrib.auth.models import User
from imageposts.models import Imagepost

from .models import Profile, Follower, Post

from multi_form_view import MultiModelFormView
from .forms import UserForm, ProfileForm
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect

# Create your views here.
def profile(request):
    return render(request, 'user/profile.html')

# DetailViews
class UserDetailView(DetailView):
    model = User
    template_name= 'user/profile.html'
    context_object_name = "user_p"

    def post(self, request, *args, **kwargs):        
        username_to_toggle = request.POST.get("username").strip()
        profile = Profile.objects.toggle_follow(request.user, username_to_toggle)
        return HttpResponseRedirect("")

    def get_context_data(self, **kwargs):
        context = super(UserDetailView,
self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        context['imagepost_list'] = Imagepost.objects.all()

        user = context['user_p']
        is_Following=False
        if (self.request.user.is_authenticated):
            if user.profile in self.request.user.is_following.all():
                is_Following=True
            context['is_following'] = is_Following

        return context

class UserImagesView(DetailView):
    model = User
    template_name= 'user/profile_images.html'
    context_object_name = "user_p"

    def post(self, request, *args, **kwargs):        
        username_to_toggle = request.POST.get("username").strip()
        profile = Profile.objects.toggle_follow(request.user, username_to_toggle)
        return HttpResponseRedirect("")

    def get_context_data(self, **kwargs):
        context = super(UserImagesView,
self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        context['imagepost_list'] = Imagepost.objects.all()

        user = context['user_p']
        is_Following=False
        if (self.request.user.is_authenticated):
            if user.profile in self.request.user.is_following.all():
                is_Following=True
            context['is_following'] = is_Following

        return context

# ListViews
class FollowerView(DetailView):
    model = User
    template_name= 'user/profile_follows.html'
    context_object_name = "user_p"

    def post(self, request, *args, **kwargs):        
        username_to_toggle = request.POST.get("username").strip()
        profile = Profile.objects.toggle_follow(request.user, username_to_toggle)
        return HttpResponseRedirect("")
        
    def get_context_data(self, **kwargs):
        context = super(FollowerView,
self).get_context_data(**kwargs)
        context['follower_list'] = Follower.objects.all()

        user = context['user_p']
        is_Following=False
        if (self.request.user.is_authenticated):
            if user.profile in self.request.user.is_following.all():
                is_Following=True
            context['is_following'] = is_Following

        return context

class UserSettingsView(MultiModelFormView):
    model = Profile
    form_classes = {
        'user_form' : UserForm,
        'profile_form' : ProfileForm,
    }
    template_name= 'user/profile_settings.html'
    context_object_name = "profile"
    def get_context_data(self, **kwargs):
        context = super(UserSettingsView,
self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        context['imagepost_list'] = Imagepost.objects.all()
        return context

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/user/login/?sgu_alert=1'
    template_name = 'registration/signup.html'    