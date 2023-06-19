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
            time_to_cook="test time to cook",
            type_of_dish=type_of_dish,
        )
        self.assertEqual(
            str(recipe),
            f"{recipe.name}"
        )

    # def test_driver_str(self):
    #     driver = get_user_model().objects.create_user(
    #         username="Test username",
    #         first_name="Test first",
    #         last_name="Test last"
    #     )
    #     self.assertEqual(
    #         str(driver),
    #         f"{driver.username} ({driver.first_name} {driver.last_name})"
    #     )
    #
    # def test_car_str(self):
    #     manufacturer = Manufacturer.objects.create(name="Test Manufacturer")
    #     car = Car.objects.create(
    #         model="Test model",
    #         manufacturer=manufacturer
    #     )
    #     self.assertEqual(str(car), car.model)
