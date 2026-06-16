# File: forms.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/16/2026
# Description: Forms for the project app.
 
from django import forms
from .models import *
 
class CreateReviewForm(forms.ModelForm):
    '''A form to add a new Review to a profile.'''

    class Meta:
        '''Associate this form with a model from our database.'''
        model = Review
        fields = ['rating', 'review_text']

class UpdateProfileForm(forms.ModelForm):
    '''A form to handle an update to an Profile.'''

    class Meta:
        '''associate this form with a model in our database.'''
        model = Profile
        fields = ['display_name', 'profile_image_url','bio_text'] # which fields we can update

class UpdateReviewForm(forms.ModelForm):
    '''A form to handle an update to an Review.'''

    class Meta:
        '''associate this form with a model in our database.'''
        model = Review
        fields = ['rating', 'review_text'] # which fields we can update

class CreateProfileForm(forms.ModelForm):
    '''A form to create a new Profile.'''

    class Meta:
        '''Associate this form with a model from our database.'''
        model = Profile
        fields = ['username', 'display_name', 'bio_text', 'profile_image_url']