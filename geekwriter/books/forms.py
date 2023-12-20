from django import forms
from .models import Book
from django.utils.translation import gettext_lazy as _


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'cover',
            'content'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'cols': 0, 'rows': 0}),
            'content': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }
        help_texts = {
            'content': _('Add documents in .pdf or .doc format')
        }
