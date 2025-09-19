from django.views.generic import TemplateView
from django.views.generic import ListView




# Create your views here.

class HomePageView(TemplateView):
    template_name = "page/home.html"


class AboutPageView(TemplateView):
    template_name = "page/about.html"


