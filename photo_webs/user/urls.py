from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.profile,name='profile'),
    path('<int:pk>/settings/', views.UserSettingsView.as_view(), name='profile-settings'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('<int:pk>/images/', views.UserImagesView.as_view(), name='profile-images'),

    path('signup/', views.SignUp.as_view(), name='signup'),
]
