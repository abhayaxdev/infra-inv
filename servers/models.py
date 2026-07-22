from django.db import models

from core.models import BaseModel


class ServerDetails(BaseModel):
    deploy = models.ForeignKey(
        "organizations.Deploy",
        on_delete=models.CASCADE,
        related_name="servers",
    )
    ip_address = models.GenericIPAddressField()
    services_used = models.TextField()

    def __str__(self):
        return f"{self.deploy} — {self.ip_address}"

    class Meta:
        verbose_name = "Server Detail"
        verbose_name_plural = "Server Details"
