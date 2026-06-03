# File: urls.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/2/2026
# Description: URL patterns for the 'mini_insta' app. Maps URL's
# to their corresponding view classes in views.py.

from django.urls import path
from .views import *

# generic view for authentication/authorization
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url to show the list of all profiles on mini_insta
    path('', ProfileListView.as_view(), name='show_all_profiles'), 

    # url to show user info for a singular profile page which is identified by the primary key
    path(r'profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'), 

    # url to show a singular post identified by the pk
    path(r'post/<int:pk>', PostDetailView.as_view(), name='show_post'), 

    # url to create a new post for a specific user profile
    path(r'profile/create_post', CreatePostView.as_view(), name='create_post'), 

    # url to update a specific profile
    path('profile/update', UpdateProfileView.as_view(), name='update_profile'), 

    # url to delete a post on a specific profile 
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'), 

    # url to update a specific post on a profile
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='update_post'), 

    # url to show all followers of a specific profile
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name='show_followers'),

    # url to show all profiles that a specific profile is following
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name='show_following'),

    # url to show post feed for a specific profile (based on their following)
    path('profile/feed', ShowFeedView.as_view(), name='show_feed'),

    # url to search for profiles and posts
    path('profile/search', SearchView.as_view(), name='search'),

    ## authorization-related URLs:
    path('login/', auth_views.LoginView.as_view(template_name='mini_insta/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='show_all_profiles'), name='logout'),

    # url to show the logged-in user their own profile page
    path('profile/', ProfileDetailView.as_view(), name='own_profile'),
]

