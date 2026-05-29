# File: forms.py
# Author: Emily Vespasiano (evespa@bu.edu), 5/27/2026
# Description: Forms for the mini_insta app.
 
from django import forms
from .models import *
 
class CreatePostForm(forms.ModelForm):
    '''A form to add a new Post to a profile.'''

    class Meta:
        '''Associate this form with a model from our database.'''
        model = Post
        fields = ['caption']