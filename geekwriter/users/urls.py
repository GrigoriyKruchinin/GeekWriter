from django.urls import path
from .views import (
    UsersListView, RegisterUserView, UserDetailView,
    UserUpdateView, UserDeleteView
)


urlpatterns = [
    path('', UsersListView.as_view(), name='writers'),
    path('registration/', RegisterUserView.as_view(), name='registration'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete')
]
