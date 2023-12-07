from django.urls import path
from .views import (
    UsersListView, RegisterUserView, UserDetailView,
    UserUpdateView, UserDeleteView
)


urlpatterns = [
    path('', UsersListView.as_view(), name='writers'),
    path('registration/', RegisterUserView.as_view(), name='registration'),
]