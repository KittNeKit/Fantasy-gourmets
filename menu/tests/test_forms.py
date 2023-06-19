from django.contrib.auth import get_user_model
from django.test import TestCase

from menu.forms import UserAccountCreationForm
from menu.models import TypeUser


class UserAccountFormTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test password"
        )
        self.client.force_login(self.user)

    def test_useraccount_creation_form_is_valid(self):
        type_of_user = TypeUser.objects.create(type="test type")
        form_data = {
            "username": "test_user1",
            "password1": "Test password123",
            "password2": "Test password123",
            "type_user": type_of_user,
            "email": "Test@email.com"
        }
        form = UserAccountCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
