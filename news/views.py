from re import template
from unicodedata import category
from attr import field
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .forms import *
class AddCategoryView(CreateView):
    model = Category
    form_class = FormCategory
    template_name = 'create_category.html'
    # fields = '__all__'

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
class DetailPostView(DeleteView):
    model = Post
    template_name = 'detail.html'