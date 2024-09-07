from django.views.generic import TemplateView, DetailView
from .models import Projects


# Create your views here.
class ProjectView(TemplateView):
    template_name = "index.html"
    model = Projects
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = self.model.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Projects
    template_name = "blog-single.html"
    context_object_name = "project"