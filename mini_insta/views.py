# File: views.py
# Author: Emily Vespasiano (evespa@bu.edu), 5/27/2026
# Description: View classes for the mini_insta app. Displays
# all mini_insta profiles and individual profile pages.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile, Post
import random

# Create your views here.
class ProfileListView(ListView):
    '''Define a view class to show all mini_insta Profiles.'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"

    # plural variable named to hold all profile objects to be displayed in the template
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    '''Display a single mini_insta profile.'''

    model = Profile
    template_name = "mini_insta/show_profile.html"
    # singular 'profile' so that you can access the object in the template
    context_object_name = "profile" 

class PostDetailView(DetailView):
    '''Display a single post'''
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"
