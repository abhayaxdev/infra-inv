from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import BaseModel
from users.manager import CustomUserManager


class CustomUser(AbstractUser, BaseModel):
    class RoleChoices(models.IntegerChoices):
        STAKEHOLDER = 1, "Stakeholder"
        PRODUCT = 2, "Product"
        DEV = 3, "Dev"
        INFRA = 4, "Infra"
        QA = 5, "QA"

    username = None
    email = models.EmailField(unique=True)
    role = models.IntegerField(
        choices=RoleChoices.choices,
        null=True,
        blank=True,
    )
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
