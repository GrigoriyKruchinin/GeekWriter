from django.urls import path
from .views import BookCreateView, BooksListView, BookDetailView


urlpatterns = [
    path('', BooksListView.as_view(), name='books'),
    path('create/', BookCreateView.as_view(), name = 'book_create'),
    path('<int:pk>/', BookDetailView.as_view(), name = 'book_detail'),

]