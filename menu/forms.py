from django import forms
from django.contrib.auth.forms import UserCreationForm

from menu.models import UserAccount, Recipe


class UserAccountCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = UserCreationForm.Meta.fields + ("type_user", "email")


class UserAccountEditForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ("first_name",
                  "last_name",
                  "email",
                  "type_user",)


class UserAccountUsernameSearchForm(forms.Form):
    username = forms.CharField(max_length=255,
                               required=False,
                               label="",
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "Search by username.."
                                   })
                               )


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"


class RecipeNameSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "Search by name.."
                               })
                           )


class GameNameSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder": "Search by name.."
                               })
                           )
