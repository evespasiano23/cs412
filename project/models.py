# File: models.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/16/2026
# Description: Data models for the project (movie review) app. Defines the Movie, Profile, Review,
# Watchlist, Follow, and Like models and their attributes such as title and date_added.

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    '''Encapsulate the data of a singular Movie.'''

    # define the data attributes of the Movie object

    # movie's title
    title = models.TextField(blank=True)

    # movies genre
    genre = models.TextField(blank=True)

    # movies release year
    year = models.IntegerField(blank=True)

    # movies director
    director = models.TextField(blank=True)

    # movie poster image url
    movie_image_url = models.TextField(blank=True)

    # movie description
    movie_description = models.TextField(blank=True)

    
    def __str__(self):
        '''Return a string representation of this Movie instance.'''
        return f'{self.title} ({self.year}) directed by {self.director}'

    def get_absolute_url(self):
        '''Return a URL to display one instance of this Movie. '''
        return reverse('show_movie', kwargs={'pk':self.pk})
    
    def get_all_reviews(self):
        '''Return all of the reviews associated with this specific movie.'''
        reviews = Review.objects.filter(movie=self).order_by('date_added')
        return reviews

    def get_average_rating(self):
        '''Return the average rating for this specific movie.'''
        reviews = self.get_all_reviews()
        if reviews.count() == 0:
            return "No reviews yet."
        return sum([r.rating for r in reviews]) / reviews.count()


class Profile(models.Model):
    '''Encapsulate the data of a single BackToTheScreen profile.'''

    # define the data attributes of the Profile object

    # profile's username 
    username = models.CharField(max_length = 30, blank=True)

    # profile user's full name shown as a heading on their profile page
    display_name = models.CharField(max_length = 40, blank=True)

    # profile user's profile picture URL
    profile_image_url = models.TextField(blank=True)

    # profile biography written by the user
    bio_text = models.TextField(blank=True)


    # links profile to a user for authentication
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this Profile instance.'''
        return f'{self.username}'

    def get_all_reviews(self):
        '''Return all Reviews by a Profile'''
        reviews = Review.objects.filter(profile=self).order_by('-date_added')
        return reviews
        
    def get_absolute_url(self):
        '''Return a URL to display one instance of this model. '''
        return reverse('show_profile', kwargs={'pk':self.pk})

    def get_followers(self):
        '''Return a list of Profiles who follow this profile.'''
        follows = Follow.objects.filter(profile=self)
        followers = []

        for follow in follows:
            followers.append(follow.follower_profile)
        return followers

    def get_num_followers(self):
        '''Returns the count of followers.'''
        return len(self.get_followers())

    def get_following(self):
        '''Returns a list of those Profiles followed by this Profile.'''
        follows = Follow.objects.filter(follower_profile=self)
        following = []

        for follow in follows:
            following.append(follow.profile)
        return following

    def get_num_following(self):
        '''Returns the count of how many Profiles a given Profile is following.'''
        return len(self.get_following())

    def get_review_feed(self):
        '''Returns a list of Reviews, specifically from the Profiles that a specific Profile follows.'''
        following = self.get_following()
        reviews = []
        for profile in following:
            profile_reviews = Review.objects.filter(profile=profile).order_by('date_added')
            reviews += list(profile_reviews)
        # sort all reviews by newest timestamp first
        reviews.sort(key=lambda post: post.date_added, reverse=True)
        return reviews 


class Review(models.Model):
    '''Encapsulate the data of a review associated with a Movie'''

    # define the data attributes of the Review object

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(blank=True, null=True) 
    review_text = models.TextField(blank=True)

    def __str__(self):
        '''Return a string representation of this Review instance.'''
        return f'{self.profile} reviewed {self.movie} at {self.date_added}.'

    def get_likes(self):
        '''Return all of the likes about this review.'''
        likes = Like.objects.filter(review=self)
        return likes
    
    def get_likes_count(self):
        '''Return the number of likes on this specific review.'''
        return self.get_likes().count()

class Watchlist(models.Model):
    '''Encapsulate the data of a Movie that is saved to a Profile's Watchlist.'''

    # define the data attributes of the Watchlist object
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Watchlist instance.'''
        return f'{self.profile} added {self.movie} to their watchlist.'

class Follow(models.Model):
    '''Encapsulate the data of a relationship between two Profiles.'''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
    follower_profile = models.ForeignKey(Profile, 
                                        on_delete=models.CASCADE, 
                                        related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Follow instance.'''
        return f'{self.follower_profile} follows {self.profile}'
    

class Like(models.Model):
    '''Encapsulate the idea of a Like about a Review.'''

    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Like.'''
        return f'{self.profile} liked {self.review} at {self.timestamp}'