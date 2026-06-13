# File: admin.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/11/2026
# Description: Registers the Joke, and Picture models
from django.contrib import admin

# Register your models here.
from .models import Joke, Picture
admin.site.register(Joke)
admin.site.register(Picture)