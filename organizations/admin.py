from django.contrib import admin

from organizations.models import DemoCredentials, Deploy, Domain, Organization, Project


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "email_contact", "website_url", "email_suffix", "is_obsolete")
    list_editable = ("is_obsolete",)
    list_filter = ("is_obsolete",)
    search_fields = ("name", "email_contact")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "is_obsolete")
    list_editable = ("is_obsolete",)
    list_filter = ("organization", "is_obsolete")
    search_fields = ("title",)


@admin.register(Deploy)
class DeployAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "environment", "is_active", "is_obsolete")
    list_editable = ("environment", "is_active", "is_obsolete")
    list_filter = ("environment", "is_active", "is_obsolete", "project__organization")
    search_fields = ("title", "project__title")


@admin.register(DemoCredentials)
class DemoCredentialsAdmin(admin.ModelAdmin):
    list_display = ("username", "user_role", "deploy", "is_obsolete")
    list_editable = ("user_role", "is_obsolete")
    list_filter = ("user_role", "is_obsolete", "deploy")
    search_fields = ("username",)


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ("url", "deploy", "is_obsolete")
    list_editable = ("is_obsolete",)
    list_filter = ("is_obsolete", "deploy")
    search_fields = ("url", "deploy__title")
