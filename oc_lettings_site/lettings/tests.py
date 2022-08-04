from django.test import TestCase, Client
from django.urls import reverse

from .models import Letting, Address


class TestLettingViews(TestCase):
    def test_letting_index(self):
        client = Client()
        response = client.get(reverse("lettings_index"))
        self.assertIs("Lettings" in str(response.content), True)
        self.assertIs("No lettings are available." in str(response.content), True)

    def test_lettings(self):
        client = Client()
        with self.assertRaises(Letting.DoesNotExist):
            client.get(reverse("letting", kwargs={"letting_id": 3}))

        address = Address.objects.create(
            number="87",
            city="Valence",
            state="Blob",
            zip_code=43,
            country_iso_code="222",
            street="rue du 4 aout",
        )
        letting = Letting.objects.create(address=address, title="Title")
        response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))
        self.assertIs("87 rue du 4 aout" in str(response.content), True)
        self.assertIs("Valence" in str(response.content), True)
        self.assertIs("222" in str(response.content), True)
