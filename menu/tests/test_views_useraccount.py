from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from menu.models import TypeUser

USEACCOUNT_LIST_URL = reverse("menu:useraccount-list")


class PublicUserAccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        type_of_user = TypeUser.objects.create(type="test type")
        get_user_model().objects.create_user(
            username="test_user_1",
            password="test password123",
            type_user=type_of_user
        )

    def setUp(self) -> None:
        self.client = Client()

    def test_login_required_useraccount(self):
        response = self.client.get(USEACCOUNT_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, "/accounts/login/?next=/user/")

    def test_login_required_useraccount_detail(self):
        useraccount_detail = get_user_model().objects.get(pk=1)
        response = self.client.get(
            reverse("menu:useraccount-detail", kwargs={"pk": useraccount_detail.pk})
        )
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, "/accounts/login/?next=/user/1/")


class PrivateUserAccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        type_of_user = TypeUser.objects.create(type="test type")
        for user_id in range(13):
            get_user_model().objects.create_user(
                username=f"test_{user_id}",
                password="test password",
                type_user=type_of_user,
            )

    def setUp(self) -> None:
        self.user = get_user_model().objects.get(pk=1)
        self.client.force_login(self.user)

    def test_useraccount_pagination_is_ten(self):
        response = self.client.get(USEACCOUNT_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["useraccount_list"]), 10)
        self.assertTemplateUsed(response, "menu/useraccount_list.html")

    def test_pagination_second_page(self):
        response = self.client.get(USEACCOUNT_LIST_URL + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["useraccount_list"]), 3)
        self.assertTemplateUsed(response, "menu/useraccount_list.html")

    def test_retrieve_useraccount_detail(self):
        useraccount_detail = get_user_model().objects.get(pk=1)
        response = self.client.get(
            reverse("menu:useraccount-detail", kwargs={"pk": useraccount_detail.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/useraccount_detail.html")

    def test_useraccount_search_result_matches_found(self):
        response = self.client.get("/user/?username=test_2")
        searching_useraccount = get_user_model().objects.filter(username="test_2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["useraccount_list"]),
            list(searching_useraccount)
        )

    def test_useraccount_search_no_matches_found(self):
        response = self.client.get("/user/?username=Fake+name")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no users.")

    def test_pagination_useraccount_search_with_value_current_page(self):
        response = self.client.get("/user/?username=Test")
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["useraccount_list"]), 10)

    def test_pagination_useraccount_search_with_value_next_page(self):
        response = self.client.get("/user/?username=Test&page=2")
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["useraccount_list"]), 3)
