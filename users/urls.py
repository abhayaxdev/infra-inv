from django.urls import path

from users.views import (
    LoginView,
    LogoutView,
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserPasswordResetView,
)

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/create/", UserCreateView.as_view(), name="user_create"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("users/<int:pk>/reset-password/", UserPasswordResetView.as_view(), name="user_password_reset"),
]
