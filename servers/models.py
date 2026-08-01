from django.db import models
from taggit.managers import TaggableManager

from core.models import BaseModel


class ServerDetails(BaseModel):
    deploy = models.ForeignKey(
        "organizations.Deploy",
        on_delete=models.CASCADE,
        related_name="servers",
    )
    name = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="Server Name"
    )
    ip_address = models.GenericIPAddressField()
    port = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(
        max_length=100, 
        blank=True, 
        null=True
    )
    services_used = models.TextField(verbose_name="Service info, port & other notes")
    provider = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    technologies = TaggableManager(verbose_name="Technologies used")
    auto_deploy = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name or self.ip_address} ({self.deploy})"

    class Meta:
        verbose_name = "Server Detail"
        verbose_name_plural = "Server Details"
