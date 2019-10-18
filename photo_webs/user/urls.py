from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.profile,name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
