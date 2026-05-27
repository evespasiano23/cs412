# File: urls.py
# Author: Emily Vespasiano (evespa@bu.edu), 5/27/2026
# Description: URL patterns for the 'mini_insta' app. Maps URL's
# to their corresponding view classes in views.py.

from django.urls import path
from .views import ProfileListView, ProfileDetailView


urlpatterns = [
    # url to show the list of all profiles on mini_insta
    path('', ProfileListView.as_view(), name='show_all_profiles'), 

    # url to show user info for a singular profile page which is identified by the primary key
    path(r'profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'), 
]

