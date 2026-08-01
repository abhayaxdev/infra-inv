from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from organizations.models import Project, Deploy


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get(self, request, *args, **kwargs):
        context  = self.get_context_data()
        context["projects"] = Project.objects.all()        
        return render(self.request, self.template_name, context)
    

@login_required
def detail_component(request, pk):
    if request.method == 'GET':
        
        if not pk:
            return HttpResponseBadRequest
        
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            messages.error(request, "The selected project does not exist")
            return redirect("core:dashboard")
        
        project = Project.objects.select_related(
            "organization",
        ).get(id=pk)
        envs = Deploy.EnvironmentChoices.choices
        
        context = {
            'project' : project,
            'deploy_envs': envs
        }
        return render(request, "partials/_detail.html", context)