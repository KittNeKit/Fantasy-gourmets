from django.contrib.auth import get_user_model
from django.test import TestCase

from menu.models import Recipe, TypeUser, Game, TypeOfDish


class ModelsTest(TestCase):
    def test_recipe_str(self):
        game = Game.objects.create(name="test game", about="game about")
        type_of_dish = TypeOfDish.objects.create(name="test type of dish")
        recipe = Recipe.objects.create(
            name="Test recipe",
            game_id=game,
            ingredients="test ingredients",
            cooking_step="test cooking step",
            time_to_cook=10,
            type_of_dish=type_of_dish,
        )
        self.assertEqual(
            str(recipe),
            f"{recipe.name}"
        )

    def test_useraccount_str(self):
        type_user = TypeUser.objects.create(type="type test")
        username = "test username"
        password = "test password"
        useraccount = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name="Test first",
            last_name="Test last",
            type_user=type_user
        )
        self.assertEqual(
            str(useraccount),
            f"{useraccount.username}"
        )
        self.assertEqual(useraccount.username, username)
        self.assertTrue(useraccount.check_password(password))

    def test_typeuser_str(self):
        type_user = TypeUser.objects.create(type="type test")
        self.assertEqual(str(type_user), type_user.type)

    def test_game_str(self):
        game = Game.objects.create(name="game test")
        self.assertEqual(str(game), game.name)

    def test_typeofdish_str(self):
        type_of_dish = TypeOfDish.objects.create(name="Dish test")
        self.assertEqual(str(type_of_dish), type_of_dish.name)
