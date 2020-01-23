from django import forms

from django.contrib.auth.models import User
from .models import Profile, Follower, Post

class UserForm(forms.ModelForm):

    class Meta(object):
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):

    class Meta(object):
        model = Profile
        fields = ['profile_img', 'profile_banner', 'bio_short', 'bio', 'location', 'show_location', 'show_email', 'birth_date']

class FollowerForm(forms.ModelForm):

    class Meta(object):
        model = Follower
        fields = ['follower', 'following']

