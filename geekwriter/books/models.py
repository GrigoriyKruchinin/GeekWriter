from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(_("title"), max_length=150)
    description = models.CharField(_("description"), max_length=550)
    cover = models.ImageField(
        verbose_name=_('cover'),
        upload_to='covers/',
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET(_('The author has been removed')),
        verbose_name=_("author"),
        related_name="author_books"
    )
    content = models.FileField(
        verbose_name=_("content"),
        upload_to='content/',
        null=False,
        blank=False,
        default='default_content.txt'
    )

    def __str__(self):
        return self.title
