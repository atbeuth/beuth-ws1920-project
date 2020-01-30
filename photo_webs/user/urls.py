from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.profile,name='profile'),
    path('settings/', views.user_edit, name='user-settings'),
    path('profile/settings/', views.profile_edit, name='profile-settings'),

    path('instagram/', views.add_insta_profile, name='profile-insta'),
    path('instagram/<int:pk>/', views.show_insta_profile, name='profile-insta-show'),

    path('settings/password/', views.change_password, name='change_password'),    path('<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('<int:pk>/images/', views.UserImagesView.as_view(), name='profile-images'),
    path('<int:pk>/bio/', views.UserBioView.as_view(), name='profile-bio'),
    path('<int:pk>/followers/', views.FollowerView.as_view(), name='profile-follows'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
