from django.urls import path

from menu.views import (
    index,
    RecipeListView,
    RecipeDetailView,
    GameListView,
    UserAccountCreateView,
    GameDetailView,
    UserAccountListView,
    UserAccountDetailView,
    RecipeCreateView,
    UserAccountFormView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "recipe/",
        RecipeListView.as_view(),
        name="recipe-list",
    ),
    path(
        "recipe/<int:pk>/",
        RecipeDetailView.as_view(),
        name="recipe-detail"
    ),
    path(
        "recipe/create/",
        RecipeCreateView.as_view(),
        name="recipe-create"
    ),
    path(
        "game/",
        GameListView.as_view(),
        name="game-list"
    ),
    path(
        "game/<int:pk>/",
        GameDetailView.as_view(),
        name="game-detail"
    ),
    path(
        "user/",
        UserAccountListView.as_view(),
        name="useraccount-list"
    ),
    path(
        "user/<int:pk>/",
        UserAccountDetailView.as_view(),
        name="useraccount-detail"
    ),
    path(
        "user/create/",
        UserAccountCreateView.as_view(),
        name="useraccount-create"),
    path(
        "user/<int:pk>/edit/",
        UserAccountFormView.as_view(),
        name="useraccount-edit"
    )
]

app_name = "menu"
