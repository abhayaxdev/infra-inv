from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=False,
        help_text="Leave blank to keep existing password.",
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "role", "organization", "is_active", "is_staff"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = CustomUser.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if not self.instance.pk and not password:
            raise forms.ValidationError("Password is required for new users.")
        return password

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p1 != p2:
            self.add_error("password2", "Passwords do not match.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "role", "organization"]


class UserPasswordResetForm(forms.Form):
    password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
    )

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned

    def save(self, user):
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user
