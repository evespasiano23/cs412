# File: forms.py
# Author: Emily Vespasiano (evespa@bu.edu), 5/29/2026
# Description: Forms for the mini_insta app.
 
from django import forms
from .models import *
 
class CreatePostForm(forms.ModelForm):
    '''A form to add a new Post to a profile.'''

    class Meta:
        '''Associate this form with a model from our database.'''
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):
    '''A form to handle an update to an Profile.'''

    class Meta:
        '''associate this form with a model in our database.'''
        model = Profile
        fields = ['display_name', 'profile_image_url','bio_text'] # which fields we can update

class UpdatePostForm(forms.ModelForm):
    '''A form to handle an update to an Post.'''

    class Meta:
        '''associate this form with a model in our database.'''
        model = Post
        fields = ['caption'] # which fields we can update