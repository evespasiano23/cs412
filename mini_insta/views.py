# mini_insta/views.py
# views for the mini_insta application
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
import random

# Create your views here.
class ProfileListView(ListView):
    '''Define a view class to show all mini_insta Profiles.'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles" # want similar to model name. will contain many instances of profile