# mini_insta/urls.py
# url patterns for the 'mini_insta' app
from django.urls import path
from .views import ProfileListView


urlpatterns = [
    path('', ProfileListView.as_view(), name='show_all_profiles'), 
]

