from django.contrib import admin
from django.urls import path
from . import views

from imageposts.views import ImagepostListView

app_name = 'web'

urlpatterns = [
    #path('', views.index,name='index'),
    path('', ImagepostListView.as_view(), name='all-imgposts'),
    path('license/', views.license,name='license'),
    path('license/de', views.license_de,name='license_de'),
]
