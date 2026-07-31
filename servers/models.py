from django.db import models

from core.models import BaseModel


class ServerDetails(BaseModel):
    deploy = models.ForeignKey(
        "organizations.Deploy",
        on_delete=models.CASCADE,
        related_name="servers",
    )
    name = models.CharField(max_length=100, blank=True, default="")
    ip_address = models.GenericIPAddressField()
    region = models.CharField(max_length=100, blank=True, default="")
    services_used = models.TextField()

    def __str__(self):
        return f"{self.name or self.ip_address} ({self.deploy})"

    class Meta:
        verbose_name = "Server Detail"
        verbose_name_plural = "Server Details"
