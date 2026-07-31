from django.contrib import admin

from servers.models import ServerDetails


@admin.register(ServerDetails)
class ServerDetailsAdmin(admin.ModelAdmin):
    list_display = ("deploy", "name", "ip_address", "region", "services_used", "is_obsolete")
    list_editable = ("name", "ip_address", "region", "services_used", "is_obsolete")
    list_filter = ("is_obsolete",)
    search_fields = ("name", "ip_address", "region", "services_used")
