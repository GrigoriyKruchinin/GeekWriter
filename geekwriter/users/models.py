from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLE_CHOICES = (
        ('author', _('Author')),
        ('reader', _('Reader')),
    )

    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='reader',
        verbose_name=_('Role'),
    )

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
