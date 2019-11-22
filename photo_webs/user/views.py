from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.models import User
from imageposts.models import Imagepost

from .models import Profile, Follower

from multi_form_view import MultiModelFormView
from .forms import UserForm, ProfileForm

# Create your views here.
def profile(request):
    return render(request, 'user/profile.html')

# DetailViews
class UserDetailView(DetailView):
    model = User
    template_name= 'user/profile.html'
    context_object_name = "user_p"
    def get_context_data(self, **kwargs):
        context = super(UserDetailView,
self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        context['imagepost_list'] = Imagepost.objects.all()
        return context

class UserImagesView(DetailView):
    model = User
    template_name= 'user/profile_images.html'
    context_object_name = "user_p"
    def get_context_data(self, **kwargs):
        context = super(UserImagesView,
self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        context['imagepost_list'] = Imagepost.objects.all()
        return context

# ListViews
class FollowerView(DetailView):
    model = User
    template_name= 'user/profile_follows.html'
    context_object_name = "user_p"
    def get_context_data(self, **kwargs):
        context = super(FollowerView,
self).get_context_data(**kwargs)
        context['follower_list'] = Follower.objects.all()
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