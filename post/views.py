from django.urls import reverse_lazy 
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import Post
from django.contrib.auth.models import User

#CRUD -> Create, Read, upate and Delete App

# The generic classes are ListView, CreateView, UpdateView, DeleteView and DetailView
#                           GET       POST         POST        POST           GET
#Create your views here.


#PostListView is going to retrieve all of the object from the Post table in the db




# Create your views here.
class PostListView(ListView): #Inheritence
  #template_name attribute is going to render an specific html file
  template_name = 'posts/list.html'
  #model is goging to be from which table we want to retrieve the data
  model = Post

  #queryset is used to define the model used for the view
  #queryset = Post.objects.all()

  # context is a python dictionary that holds the data for the generic views
  # and this context travels to the htmls
  # by default the context name of ListView and DetailView is object or object_list

  #context_object_nmae would allow us to modify the name and how to call it in the htmls
  context_object_name = 'post_list'


class PostDetailView(DetailView):
  template_name = "posts/detail.html"
  model = Post 
  context_object_name = "single_post"
  
  


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post 
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
      print(form)
      print(User.object.all())
      form.instance.author = User.objects.filter(is_superuser=True).first()
      return super().form_valid(form)
    
  #PostDeleteView is going to allow us delete an existing record from the db

class PostDeleteView(DeleteView):
  template_name = "posts/delete.html"
  model = Post 
  success_url = reverse_lazy ("posts")
  

#PostUpdateView is going to allow us to edit existing records from the db

class PostUpdateView(UpdateView):
  template_name = "post/edit.html"
  model = Post
  fields = ["title", "subtitle", "body"]


