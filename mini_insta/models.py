# File: models.py
# Author: Emily Vespasiano (evespa@bu.edu), 5/27/2026
# Description: Data models for the mini_insta app. Defines the Profile model and 
# its attributes such as username and join date.

from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Encapsulate the data of a single mini_insta profile.'''

    # define the data attributes of the Profile object

    # profile's username 
    username = models.TextField(blank=True)

    # profile user's full name shown as a heading on their profile page
    display_name = models.TextField(blank=True)

    # profile user's profile picture URL
    profile_image_url = models.TextField(blank=True)

    # profile biography written by the user
    bio_text = models.TextField(blank=True)

    # profile user's Instagram join date
    join_date = models.DateField(blank=True)

    def __str__(self):
        '''return a string representation of this Profile instance'''
        return f'{self.username}'

    def get_all_posts(self):
        '''Return all posts by a profile'''
        posts = Post.objects.filter(profile=self).order_by('timestamp')
        return posts

class Post(models.Model):
    '''Encapsulate the data of a post by a profile'''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    
    def __str__(self):
        '''return a string representation of this Post instance'''
        return f'Post by {self.profile} at {self.timestamp}'

    def get_absolute_url(self):
        '''Return a URL to display one instance of this Post. '''
        return reverse('show_post', kwargs={'pk':self.pk})
    
    def get_all_photos(self):
        '''Return all of the photos associated with a specific post.'''
        photos = Photo.objects.filter(post=self).order_by('timestamp')
        return photos

class Photo(models.Model):
    '''Encapsulate the data of a photo associated with a post'''

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    image_file = models.ImageField(blank=True) # an actual image

    def __str__(self):
        '''return a string representation of this Photo instance'''
        if self.image_url:
            return f'Photo url {self.image_url} at {self.timestamp}'
        return f'Photo file {self.image_file} at {self.timestamp}'

    def get_image_url(self):
        '''returns the URL to the image'''
        if self.image_url:
            return self.image_url
        return self.image_file.url