from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from menu.models import Recipe, Game, TypeOfDish, TypeUser

RECIPE_LIST_URL = reverse("menu:recipe-list")


class PublicRecipeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        game = Game.objects.create(name="Test Game")
        type_of_dish = TypeOfDish.objects.create(name="Test TypeOfDish")
        Recipe.objects.create(name="Test 1",
                              game_id=game,
                              time_to_cook=20,
                              type_of_dish=type_of_dish)
        Recipe.objects.create(name="Test 2",
                              game_id=game,
                              time_to_cook=20,
                              type_of_dish=type_of_dish)

    def setUp(self) -> None:
        self.client = Client()

    def test_login_required_recipe_list(self):
        response = self.client.get(RECIPE_LIST_URL)
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, "/accounts/login/?next=/recipe/")

    def test_login_required_recipe_detail(self):
        recipe_detail = Recipe.objects.get(pk=1)
        response = self.client.get(
            reverse("menu:recipe-detail", kwargs={"pk": recipe_detail.pk})
        )
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, "/accounts/login/?next=/recipe/1/")

    def test_login_required_creation_recipe_form(self):
        response = self.client.get(reverse("menu:recipe-create"))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, "/accounts/login/?next=/recipe/create/")


class PrivateRecipeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        game = Game.objects.create(name="Test Game")
        type_of_dish = TypeOfDish.objects.create(name="Test TypeOfDish")
        for recipe_id in range(13):
            Recipe.objects.create(
                name=f"Test {recipe_id}",
                game_id=game,
                time_to_cook=20,
                type_of_dish=type_of_dish
            )

    def setUp(self) -> None:
        type_of_user_chef = TypeUser.objects.create(type="Chef")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test password",
            type_user=type_of_user_chef,
        )
        self.client.force_login(self.user)

    def test_recipe_pagination_is_ten(self):
        response = self.client.get(RECIPE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["recipe_list"]), 10)
        self.assertTemplateUsed(response, "menu/recipe_list.html")

    def test_recipe_pagination_second_page(self):
        response = self.client.get(RECIPE_LIST_URL + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["recipe_list"]), 3)
        self.assertTemplateUsed(response, "menu/recipe_list.html")

    def test_retrieve_recipe_detail(self):
        recipe_detail = Recipe.objects.get(pk=1)
        response = self.client.get(
            reverse("menu:recipe-detail", kwargs={"pk": recipe_detail.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "menu/recipe_detail.html")

    def test_create_recipe_btn_only_for_chef(self):
        response = self.client.get(RECIPE_LIST_URL)
        self.assertContains(response, "add recipe!")

    def test_recipe_search_matches_found(self):
        response = self.client.get("/recipe/?name=test+2")
        searching_recipe = Recipe.objects.filter(name="Test 2")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["recipe_list"]),
            list(searching_recipe)
        )

    def test_recipe_search_no_matches_found(self):
        response = self.client.get("/recipe/?name=Fake+name")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no recipe.")
