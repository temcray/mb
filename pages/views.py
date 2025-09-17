from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post



# Create your views here.

class HomePageView(TemplateView):
    template_name = "page/home.html"


class AboutPageView(TemplateView):
    template_name = "page/about.html"


class PostListViews(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "list/post"