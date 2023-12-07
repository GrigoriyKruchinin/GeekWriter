from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "password1",
            "password2",
        )



class UpdateUserForm(UserChangeForm):
    pass
