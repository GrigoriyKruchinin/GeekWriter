from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class CustomPermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().id != request.user.id:
            messages.error(
                request, _("You don't have permission to modify another user.")
            )
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)


class MyLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _("You are not logged in! Please log in!"))
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)
