from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

def profile(request):
    return render(request, 'user/profile.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/user/login/?sgu_alert=1'
    template_name = 'registration/signup.html'