# File: serializers.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/11/2026
# Description: Serializers for the dadjokes app. Converts the Joke and Picture
# models to JSON format for the REST API.
 
from rest_framework import serializers
from .models import *
 
class JokeSerializer(serializers.ModelSerializer):
  '''
  A serializer for the Joke model.
  Specify which model/fields to send in the API.
  '''
 
  class Meta:
    model = Joke
    fields = ['id', 'text', 'contributor', 'timestamp']
   
  # add methods to customize the Create/Read/Update/Delete operations
  def create(self, validated_data):
    '''
    Override the superclass method that handles object creation.
    '''
    print(f'JokeSerializer.create, validated_data={validated_data}.')

    # do the create and save all at once
    return Joke.objects.create(**validated_data)

class PictureSerializer(serializers.ModelSerializer):
  '''
  A serializer for the Picture model.
  Specify which model/fields to send in the API.
  '''
 
  class Meta:
    model = Picture
    fields = ['id', 'image_url', 'contributor', 'timestamp']