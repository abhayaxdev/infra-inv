from django.urls import path
from django.views.generic import TemplateView

from core.views import *

app_name = "core"

urlpatterns = [
    path("", TemplateView.as_view(template_name="core/landing.html"), name="landing"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("detail/", detail_component, name="project_detail"),
]
