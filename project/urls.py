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
    # url to show the list of all movies on BackToTheScreen (project)
    path('', MovieListView.as_view(), name='show_all_movies'), 

    # url to show user info for a singular movie page which is identified by the primary key
    path(r'movie/<int:pk>', MovieDetailView.as_view(), name='show_movie'), 

    # url to show a singular review identified by the pk
    path(r'review/<int:pk>', ReviewDetailView.as_view(), name='show_review'), 

    # url to create a new review for a specific user profile
    path(r'profile/create_review', CreateReviewView.as_view(), name='create_review'), 

    # url to update a specific profile
    path('profile/update', UpdateProfileView.as_view(), name='update_profile'), 

    # ADD MORE LATER
]

