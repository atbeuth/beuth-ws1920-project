from django.urls import path
from imageposts.views import ImagepostListView

from . import views

app_name = "web"

urlpatterns = [
    path("", ImagepostListView.as_view(), name="all-imgposts"),
    path("license/", views.license, name="license"),
    path("license/de/", views.license_de, name="license_de"),
    path("imprint/", views.imprint, name="imprint"),
    path("imprint/de/", views.imprint_de, name="imprint_de"),
    path("license/de", views.license_de, name="license_de"),
    path("search/<str:pk>", views.search, name="search"),
]
