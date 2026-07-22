from django.contrib import admin

from servers.models import ServerDetails


@admin.register(ServerDetails)
class ServerDetailsAdmin(admin.ModelAdmin):
    list_display = ("deploy", "ip_address", "services_used", "is_obsolete")
    list_editable = ("services_used", "is_obsolete")
    list_filter = ("is_obsolete",)
    search_fields = ("ip_address", "services_used")
