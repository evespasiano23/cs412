# File: views.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/11/2026
# Description: View classes for the dadjokes app. Displays
# all dadjokes Jokes and Pictures and REST API views.
from django.views.generic import ListView, DetailView
from .models import Joke, Picture
from rest_framework import generics
from .serializers import *
import random

class ShowAllJokesView(ListView):
    '''Define a view class to show all Jokes.'''
    model = Joke
    template_name = "dadjokes/show_all_jokes.html"
    context_object_name = "jokes"

class ShowJokeView(DetailView):
    '''Display a single joke.'''
    model = Joke
    template_name = "dadjokes/show_joke.html"
    context_object_name = "joke"

class ShowAllPicturesView(ListView):
    '''Define a view class to show all Pictures'''
    model = Picture
    template_name = "dadjokes/show_all_pictures.html"
    context_object_name = "pictures"

class ShowPictureView(DetailView):
    '''Display a single picture.'''
    model = Picture
    template_name = "dadjokes/show_picture.html"
    context_object_name = "picture"

class RandomView(DetailView):
    '''Display one random Joke and Picture selected at random.'''

    model = Joke
    template_name = "dadjokes/random.html"
    context_object_name = "joke"

    def get_object(self):
        '''return one instance of the Joke object
        selected at random.'''
        return random.choice(list(Joke.objects.all()))

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
        context = super().get_context_data(**kwargs)
        context['picture'] = random.choice(list(Picture.objects.all()))
        return context

class JokeListAPIView(generics.ListCreateAPIView):
  '''
  An API view to return a listing of Jokes 
  and to create an Joke.
  '''
  queryset = Joke.objects.all()
  serializer_class = JokeSerializer
 
class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''An API view to return a single joke using the primary key.'''
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class PictureListAPIView(generics.ListCreateAPIView):
  '''
  An API view to return a listing of Pictures 
  and to create an Picture.
  '''
  queryset = Picture.objects.all()
  serializer_class = PictureSerializer
 
class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''An API view to return a single picture using the primary key.'''
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
 
class RandomJokeAPIView(generics.RetrieveAPIView):
  '''
  An API view to return a random joke
  '''
  serializer_class = JokeSerializer

  def get_object(self):
    '''return one Joke chosen randomly.'''
    jokes = Joke.objects.all()
    return random.choice(list(jokes))

class RandomPictureAPIView(generics.RetrieveAPIView):
  '''
  An API view to return a random picture
  '''
  serializer_class = PictureSerializer

  def get_object(self):
    '''return one Picture chosen randomly.'''
    pictures = Picture.objects.all()
    return random.choice(list(pictures))
 
