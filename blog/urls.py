# blog/urls.py
# url patterns for the 'blog' app
from django.urls import path
from .views import ShowAllView


urlpatterns = [
    path('', ShowAllView.as_view(), name='show_all'), 
    # path(r'order', views.order, name='order'), 
    # path('confirmation', views.confirmation, name='confirmation'),

]