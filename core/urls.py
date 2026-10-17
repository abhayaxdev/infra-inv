from django.urls import path
from django.views.generic import TemplateView

from core.views import *

app_name = "core"

urlpatterns = [
    path("", TemplateView.as_view(template_name="core/landing.html"), name="landing"),
    path("random/", TemplateView.as_view(template_name="core/random.html"), name="random"),
    path("pr-flow/", TemplateView.as_view(template_name="core/pr_flow.html"), name="pr_flow"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("detail/<int:pk>/", detail_component, name="project_detail"),
]
