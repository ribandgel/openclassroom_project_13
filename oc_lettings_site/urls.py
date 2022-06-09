from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'), path("admin/", admin.site.urls), url("lettings/", include("oc_lettings_site.lettings.urls")), url("profiles/", include("oc_lettings_site.profiles.urls"))]
