# blogs/views.py
# views for the blog application
from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

# Create your views here.
class ShowAllView(ListView):
    '''Define a view class to show all blog Articles.'''

    model = Article
    template_name = "blog/show_all.html"
    context_object_name = "articles" # want similar to model name. will contain many instances of article