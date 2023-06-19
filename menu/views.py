from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from menu.forms import (
    UserAccountCreationForm,
    RecipeForm,
    UserAccountEditForm,
    UserAccountUsernameSearchForm,
    GameNameSearchForm,
    RecipeNameSearchForm
)
from menu.models import (
    Game,
    TypeOfDish,
    Recipe,
    UserAccount
)


def index(request):
    num_game = Game.objects.count()
    num_type_of_dish = TypeOfDish.objects.count()
    num_recipe = Recipe.objects.count()

    context = {
        "num_game": num_game,
        "num_type_of_dish": num_type_of_dish,
        "num_recipe": num_recipe
    }
    return render(request, "menu/index.html", context=context)


class RecipeListView(LoginRequiredMixin, generic.ListView):
    model = Recipe
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = RecipeNameSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = Recipe.objects.all()
        form = RecipeNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class RecipeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Recipe


class RecipeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("menu:recipe-list")


class GameListView(LoginRequiredMixin, generic.ListView):
    model = Game

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = GameNameSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = Game.objects.all()
        form = GameNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class GameDetailView(LoginRequiredMixin, generic.DetailView):
    model = Game

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        recipe = Recipe.objects.filter(game_id=kwargs["object"].pk)
        context["recipe_list"] = recipe
        return context


class UserAccountCreateView(generic.CreateView):
    model = UserAccount
    form_class = UserAccountCreationForm
    template_name = "registration/sign-up.html"
    success_url = reverse_lazy("menu:index")


class UserAccountListView(LoginRequiredMixin, generic.ListView):
    model = UserAccount
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAccountListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = UserAccountUsernameSearchForm(
            initial={
                "username": username
            }
        )
        return context

    def get_queryset(self):
        queryset = UserAccount.objects.all()
        form = UserAccountUsernameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )


class UserAccountDetailView(LoginRequiredMixin, generic.DetailView):
    model = UserAccount


class UserAccountFormView(LoginRequiredMixin, generic.UpdateView):
    model = UserAccount
    form_class = UserAccountEditForm
    success_url = reverse_lazy("menu:useraccount-list")


class LogoutView(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, "menu/index.html")
