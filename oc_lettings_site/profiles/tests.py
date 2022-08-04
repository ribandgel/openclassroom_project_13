from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


class TestProfileViews(TestCase):
    def test_profile_index(self):
        client = Client()
        response = client.get(reverse("profiles_index"))
        self.assertIs("Profiles" in str(response.content), True)
        self.assertIs("Lettings" in str(response.content), True)

    def test_profiles(self):
        client = Client()
        user = User.objects.create(username="blob")
        with self.assertRaises(Profile.DoesNotExist):
            client.get(reverse("profile", kwargs={"username": "blob"}))
        Profile.objects.create(user=user, favorite_city="Valence")
        response = client.get(reverse("profile", kwargs={"username": "blob"}))
        self.assertIs("Favorite city: Valence" in str(response.content), True)
