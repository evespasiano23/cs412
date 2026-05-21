# restaurant/urls.py
# url patterns for the 'restaurant' app

from django.urls import path
from django.conf import settings
from . import views

# URL patterns for this app:
urlpatterns = [
    path(r'', views.main, name='main'), 
    path(r'order', views.order, name='order'), # update as you go 
    path('confirmation', views.confirmation, name='confirmation'),

]
