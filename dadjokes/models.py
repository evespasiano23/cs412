# File: models.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/11/2026
# Description: Data models for the dadjokes app. Defines the Joke, and Picture
# models and their attributes such as contributor and image_url.
from django.db import models

# Create your models here.
class Joke(models.Model):
    '''Encapsulate the data of a dad joke.'''

    text = models.TextField(blank=False) # the text of the joke
    contributor = models.TextField(blank=False) # the name of the joke contributor
    timestamp = models.DateTimeField(auto_now=True) # the time the joke was created

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.text} by {self.contributor}'

class Picture(models.Model):
    '''Encapsulate the data of a picture.'''
    image_url = models.URLField(blank=False) # the URL of the picture
    contributor = models.TextField(blank=False) # the name of the picture contributor
    timestamp = models.DateTimeField(auto_now=True) # the time the picture was created

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'Picture created by {self.contributor}'