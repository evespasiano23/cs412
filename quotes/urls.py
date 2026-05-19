# file: quotes/url.py

from django.urls import path
from . import views

# URL patterns specific to the quotes app:
urlpatterns = [
    path(r'', views.quote, name="quote"),
    path(r'quote', views.quote, name="quote"),
    path(r'show_all', views.show_all, name="show_all"),
    path(r'about', views.about, name="about"),
    
]   