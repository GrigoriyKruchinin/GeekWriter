import django.contrib.messages.views
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CreateUserForm, UpdateUserForm
from .models import User

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


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
    pass


class UserUpdateView(UpdateView):
    pass


class UserDeleteView(DeleteView):
    pass
