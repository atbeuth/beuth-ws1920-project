from django.contrib import admin
from django.urls import path
from . import views

from imageposts.views import ImagepostListView

app_name = 'web'

urlpatterns = [
    path('', ImagepostListView.as_view(), name='all-imgposts'),
    path('license/', views.license,name='license'),
    path('license/de', views.license_de,name='license_de'),
    path('search/<str:pk>', views.search,name='search'),
]
