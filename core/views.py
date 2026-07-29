from django.views.generic import TemplateView
from django.shortcuts import render

from organizations.models import Project


class Dashboard(TemplateView):
    template_name = "core/dashboard.html"

    def get(self, request, *args, **kwargs):
        context  = self.get_context_data()
        context["projects"] = Project.objects.all()        
        return render(self.request, self.template_name, context)
    

def detail_component(request):
    if request.method == 'GET':
        return render(request, "partials/_detail.html")