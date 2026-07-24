from django.urls import path
from django.views.generic import TemplateView

app_name = "core"

urlpatterns = [
    path("", TemplateView.as_view(template_name="core/landing.html"), name="landing"),
    path("dashboard/", TemplateView.as_view(template_name="core/dashboard.html"), name="dashboard"),
]
