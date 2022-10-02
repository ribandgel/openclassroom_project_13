from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from . import views


def trigger_error(request):
    division_by_zero = 1
    division_by_zero = division_by_zero / 0


urlpatterns = [
    path("", views.index, name="index"),
    path("sentry-debug/", trigger_error, name="sentry-debug"),
    path("admin/", admin.site.urls),
    path("lettings/", include("oc_lettings_site.lettings.urls"), name="lettings"),
    path("profiles/", include("oc_lettings_site.profiles.urls"), name="profiles"),
]
