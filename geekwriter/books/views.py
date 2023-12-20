import django.contrib
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)
from .models import Book
from .forms import BookForm

from django.contrib.messages.views import SuccessMessageMixin

from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

class BookCreateView(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books')
    success_message = _('Book is successfully created')
    extra_context = {
        'header': _('Create book'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BooksListView(ListView):
    template_name = 'books/books.html'
    model = Book
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'