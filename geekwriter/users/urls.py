from django.urls import path
from .views import (
    UsersListView, RegisterUserView, UserDetailView,
    UserUpdateView, UserDeleteView
)


urlpatterns = [
    path('registration/', RegisterUserView.as_view(), name='registration'),
]