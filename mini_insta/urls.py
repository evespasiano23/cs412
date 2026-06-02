# File: urls.py
# Author: Emily Vespasiano (evespa@bu.edu), 5/29/2026
# Description: URL patterns for the 'mini_insta' app. Maps URL's
# to their corresponding view classes in views.py.

from django.urls import path
from .views import ProfileListView, ProfileDetailView, PostDetailView, CreatePostView, UpdateProfileView


urlpatterns = [
    # url to show the list of all profiles on mini_insta
    path('', ProfileListView.as_view(), name='show_all_profiles'), 

    # url to show user info for a singular profile page which is identified by the primary key
    path(r'profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'), 

    # url to show a singular post identified by the pk
    path(r'post/<int:pk>', PostDetailView.as_view(), name='show_post'), 

    # url to create a new post for a specific user profile
    path(r'profile/<int:pk>/create_post', CreatePostView.as_view(), name='create_post'), 

    # url to update a specific profile
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'), 
]

