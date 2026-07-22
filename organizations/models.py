from django.db import models

from core.fields import EncryptedTextField
from core.models import BaseModel


class Organization(BaseModel):
    name = models.CharField(max_length=255)
    email_contact = models.EmailField(null=True, blank=True)
    website_url = models.URLField(null=True, blank=True)
    email_suffix = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"


class Project(BaseModel):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="projects",
    )
    title = models.CharField(max_length=255, verbose_name="Project Title")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Deploy(BaseModel):
    class EnvironmentChoices(models.IntegerChoices):
        DEV = 1, "Development"
        STAGING = 2, "Staging"
        UAT = 3, "UAT"
        PROD = 4, "Production"

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="deployments",
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    environment = models.IntegerField(
        choices=EnvironmentChoices.choices,
        default=EnvironmentChoices.DEV,
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.project}-{self.title} — {self.get_environment_display()}"

    class Meta:
        verbose_name = "Deploy"
        verbose_name_plural = "Deploys"


class Domain(BaseModel):
    deploy = models.ForeignKey(
        Deploy,
        on_delete=models.CASCADE,
        related_name="domains",
    )
    url = models.URLField()

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"


class Credential(BaseModel):
    deploy = models.ForeignKey(
        Domain,
        on_delete=models.CASCADE,
        related_name="credentials",
    )
    username = models.CharField(max_length=255)
    password = EncryptedTextField()
    user_role = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.deploy})"

    class Meta:
        verbose_name = "Credential"
        verbose_name_plural = "Credentials"


