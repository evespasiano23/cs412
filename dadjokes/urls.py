# File: urls.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/11/2026
# Description: URL patterns for the 'dadjokes' app. Maps URL's
# to their corresponding view classes in views.py.
from django.urls import path, include
from .views import * 


urlpatterns = [
    # url to show one Joke and one Picture selected at random
    path('', RandomView.as_view(), name='random'),

    # url to show one Joke and one Picture selected at random
    path('random', RandomView.as_view(), name='random'),

    # url to show a page with all Jokes (no images)
    path('jokes', ShowAllJokesView.as_view(), name='show_all_jokes'),

    # url to show one Joke by its primary key
    path('joke/<int:pk>', ShowJokeView.as_view(), name='show_joke'),

    # url to show a page with all Pictures (no jokes)
    path('pictures', ShowAllPicturesView.as_view(), name='show_all_pictures'),

    # url to show one Picture by its primary key
    path('picture/<int:pk>', ShowPictureView.as_view(), name='show_picture'),

    # returns a Json representation of one Joke selected at random
    path(r'api/', RandomJokeAPIView.as_view()),

    # returns a Json representation of one Joke selected at random
    path(r'api/random', RandomJokeAPIView.as_view()),

    # returns a Json representation of all Jokes
    path(r'api/jokes', JokeListAPIView.as_view()),

    # returns a Json representation of one Joke by its primary
    path(r'api/joke/<int:pk>', JokeDetailAPIView.as_view()),

    # returns a Json representation of all Pictures
    path(r'api/pictures', PictureListAPIView.as_view()),

    # returns a Json representation of one Picture by its primary key
    path(r'api/picture/<int:pk>', PictureDetailAPIView.as_view()),

    # returns a Json representation of one Picture selected at random
    path(r'api/random_picture', RandomPictureAPIView.as_view()),
]