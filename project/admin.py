# File: admin.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/16/2026
# Description: Registers the Movie, Profile, Review, Watchlist, Follow, and Like models
from django.contrib import admin

# Register your models here.
from .models import Movie, Profile, Review, Watchlist, Follow, Like

admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Watchlist)
admin.site.register(Follow)
admin.site.register(Like)