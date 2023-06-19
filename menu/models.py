from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class TypeUser(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class UserAccount(AbstractUser):
    type_user = models.ForeignKey(
        TypeUser,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("menu:useraccount-detail", kwargs={"pk": self.pk})


class Game(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse("menu:game-detail", kwargs={"pk": self.pk})


class TypeOfDish(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    ingredients = models.TextField()
    cooking_step = models.TextField()
    time_to_cook = models.IntegerField()
    type_of_dish = models.ForeignKey(TypeOfDish, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("menu:recipe-detail", kwargs={"pk": self.pk})
