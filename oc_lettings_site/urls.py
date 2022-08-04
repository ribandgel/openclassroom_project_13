from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("", views.index, name="index"),
    path('sentry-debug/', trigger_error),
    path("admin/", admin.site.urls),
    path("lettings/", include("oc_lettings_site.lettings.urls")),
    path("profiles/", include("oc_lettings_site.profiles.urls")),
]
