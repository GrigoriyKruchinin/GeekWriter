from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CreateUserForm, UpdateUserForm
from .models import User

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from geekwriter.mixins import CustomPermissionMixin, MyLoginRequiredMixin


class UsersListView(ListView):
    model = User
    template_name = 'users/writers.html'
    context_object_name = 'users'


class RegisterUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'form.html'
    success_message = _("You have been successfully registered")
    success_url = reverse_lazy("login")
    extra_context = {
        "header": _("Registration"),
        "button_text": _("Create user")
    }


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'


class UserUpdateView(
    MyLoginRequiredMixin, CustomPermissionMixin,
    SuccessMessageMixin, UpdateView
):
    model = User
    form_class = UpdateUserForm
    template_name = 'form.html'
    success_message = _("You have been successfully updated your information")
    success_url = reverse_lazy('home')
    extra_context = {
        'header': _("Update own information"),
        'button_text': _("Update")
    }


class UserDeleteView(DeleteView):
    pass
