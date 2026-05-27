# marathon_analytics/urls.py
# url patterns for the 'marathon_analytics' app

from django.urls import path
from . import views

# URL patterns for this app:
urlpatterns = [
    # map the URL (empty string) to the view
    path(r'', views.ResultListView.as_view(), name='home'), 
    path(r'results', views.ResultListView.as_view(), name='results_list'), 

]