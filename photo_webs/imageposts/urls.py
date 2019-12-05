from django.contrib import admin
from django.urls import path
from . import views

app_name = 'imageposts'

urlpatterns = [
    path('post/', views.add_post, name='add-post'),

]
