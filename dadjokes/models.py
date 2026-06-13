# blog/models.py
# define data models for the blog application
from django.db import models

# Create your models here.
class Joke(models.Model):
    '''Encapsulate the data of a dad joke.'''

    text = models.TextField(blank=False)
    contributor = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.text} by {self.contributor}'

class Picture(models.Model):
    '''Encapsulate the data of a picture.'''
    image_url = models.URLField(blank=False)
    contributor = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'Picture created by {self.contributor}'