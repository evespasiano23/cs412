# blog/forms.py
# define the forms that we use for create/update/delete operations
 
 
from django import forms
from .models import Article
 
class CreateArticleForm(forms.ModelForm):
    '''A form to add an Article to the database.'''

    class Meta:
        '''Associate this form with a model from our database.'''
        model = Article
        fields = ['author', 'title', 'text', 'image_url']