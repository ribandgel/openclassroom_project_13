from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("lettings/", include("oc_lettings_site.lettings.urls")),
    path("profiles/", include("oc_lettings_site.profiles.urls")),
]
