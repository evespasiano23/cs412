# File: models.py
# Author: Emily Vespasiano (evespa@bu.edu), 5/27/2026
# Description: Data models for the mini_insta app. Defines the Profile model and 
# its attributes such as username and join date.

from django.db import models

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