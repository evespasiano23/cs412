# File: urls.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/16/2026
# Description: URL patterns for the 'project' app. Maps URL's
# to their corresponding view classes in views.py.

from django.urls import path
from .views import *

# generic view for authentication/authorization
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    # url to show the list of all movies on BackToTheScreen
    path('', MovieListView.as_view(), name='show_all_movies'),

    # url to show the randomly chosen movie of the day which resets/changes every 24 hours
    path('movie_of_the_day', MovieOfTheDayView.as_view(), name='movie_of_the_day'),

    # url to show user info for a singular profile page identified by the primary key
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),

    # url to show a singular movie page identified by the primary key
    path('movie/<int:pk>', MovieDetailView.as_view(), name='show_movie'),

    # url to create a new review for a specific movie
    path('movie/<int:pk>/create_review', CreateReviewView.as_view(), name='create_review'),

    # url to update a specific profile
    path('profile/update', UpdateProfileView.as_view(), name='update_profile'),

    # url to delete a specific review
    path('review/<int:pk>/delete', DeleteReviewView.as_view(), name='delete_review'),

    # url to update a specific review
    path('review/<int:pk>/update', UpdateReviewView.as_view(), name='update_review'),

    # url to show all followers of a specific profile
    path('profile/<int:pk>/followers', ShowFollowersDetailView.as_view(), name='show_followers'),

    # url to show all profiles that a specific profile is following
    path('profile/<int:pk>/following', ShowFollowingDetailView.as_view(), name='show_following'),

    # url to show review feed for a specific profile (based on their following)
    path('feed', ShowFeedView.as_view(), name='show_feed'),

    # url to search for movies and profiles
    path('search', SearchView.as_view(), name='search'),

    ## authorization-related URLs:
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='project_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='logout_confirmation_project'), name='project_logout'),

    # url to show the logged-in user their own profile page
    path('profile/', ProfileDetailView.as_view(), name='own_profile'),

    # url to show the user the logout confirmation page
    path('logout_confirmation/', TemplateView.as_view(template_name='project/logged_out.html'), name='logout_confirmation_project'),

    # url to create a new profile
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),

    # url to follow a profile
    path('profile/<int:pk>/follow', FollowProfileView.as_view(), name='follow_profile'),

    # url to unfollow a profile
    path('profile/<int:pk>/delete_follow', UnfollowProfileView.as_view(), name='unfollow_profile'),

    # url to like a review
    path('review/<int:pk>/like', LikeReviewView.as_view(), name='like_review'),

    # url to unlike a review
    path('review/<int:pk>/delete_like', UnlikeReviewView.as_view(), name='unlike_review'),

    # url to add a movie to a profile's watchlist
    path('movie/<int:pk>/add_watchlist', AddToWatchlistView.as_view(), name='add_watchlist'),

    # url to remove a movie from a profile's watchlist
    path('movie/<int:pk>/remove_watchlist', RemoveFromWatchlistView.as_view(), name='remove_watchlist'),

    # url to show a profile's watchlist 
    path('profile/<int:pk>/watchlist', ShowWatchlistView.as_view(), name='show_watchlist'),
]

