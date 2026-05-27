# marathon_analytics/views.py
from django.shortcuts import render

# Create your views here.
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from . models import Result

class ResultListView(ListView):
    '''View to display marathon results.'''

    model = Result
    template_name = 'marathon_analytics/results.html'
    context_object_name = 'results'
    paginate_by = 25 # how many records per page

    def get_queryset(self):
        ''' limit the result queryset (for now).'''
        results = super().get_queryset()
    #     return results[:25] # slice to only return first 25 records

        # look for URL parameters to filter by:
        if 'city' in self.request.GET:
            city = self.request.GET['city']

            if city:
                results = results.filter(city=city)

            return results