from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView

from users.models import CustomUser
from users.forms import UserForm, UserPasswordResetForm


class LoginView(BaseLoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True


class LogoutView(BaseLogoutView):
    next_page = reverse_lazy("core:landing")


class SuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        messages.error(self.request, "Only superusers can access this page.")
        return redirect("core:dashboard")


class UserListView(SuperuserRequiredMixin, ListView):
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"
    ordering = ["email"]


class UserCreateView(SuperuserRequiredMixin, SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:user_list")
    success_message = "User created successfully."


class UserUpdateView(SuperuserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = UserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:user_list")
    success_message = "User updated successfully."


class UserDeleteView(SuperuserRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("users:user_list")


class UserPasswordResetView(SuperuserRequiredMixin, SuccessMessageMixin, FormView):
    template_name = "users/user_password_reset.html"
    form_class = UserPasswordResetForm
    success_message = "Password reset successfully."

    def dispatch(self, request, *args, **kwargs):
        self.user_obj = CustomUser.objects.get(pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["target_user"] = self.user_obj
        return context

    def form_valid(self, form):
        form.save(self.user_obj)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("users:user_list")
