# File: admin.py
# Author: Emily Vespasiano (evespa@bu.edu), 5/29/2026
# Description: Registers the Profile, Post, and Photo models
from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Photo

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)