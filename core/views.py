from django.shortcuts import render
from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name_page"] = 'Web Playground'
        return context
    

class SampleTemplateView(TemplateView):
    template_name = 'core/sample.html'
