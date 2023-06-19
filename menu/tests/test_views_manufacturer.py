from django.test import TestCase, Client
from django.urls import reverse

GAME_LIST_URL = reverse("menu:game-list")


class PublicGameTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_manufacturers_list_login_required(self):
        response = self.client.get(GAME_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, "/accounts/login/?next=/game/")
