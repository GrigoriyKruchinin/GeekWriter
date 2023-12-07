from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    success_message = _("You are logged in")
    next_page = reverse_lazy('home')
    extra_context = {
        'header': _("Log in"),
        'button_text': _("Log in")
    }


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
