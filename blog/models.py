# blog/models.py
# define data models for the blog application
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    '''Encapsulate the data of a blog Article by an author.'''

    # define the data attributes of the Article object
    title = models.TextField(blank=True)
    author = models.TextField(blank=True)
    text = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        '''return a string representation of this model instance'''
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        '''Return a URL to display one instance of this model. '''
        return reverse('article', kwargs={'pk':self.pk})