# File: views.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/16/2026
# Description: View classes for the project app. Displays
# all BackToTheScreen movies, profiles, and reviews.
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin ## for authentication
from django.contrib.auth.forms import UserCreationForm ## for new user
from django.contrib.auth import login
from datetime import date

class ProfileLoginMixin(LoginRequiredMixin):
    '''Mixin class that handles login requirements for views classes.'''

    def get_login_url(self):
        '''return the URL for this app's login page'''
        return reverse('login')

    def get_current_profile(self):
        '''return the current profile user logged in'''
        return Profile.objects.get(user=self.request.user)

class MovieListView(ListView):
    '''Define a view class to show all Movies.'''

    model = Movie
    template_name = "project/show_all_movies.html"
    context_object_name = "movies"

class MovieDetailView(DetailView):
    '''Display a single project Movie.'''

    model = Movie
    template_name = "project/show_movie.html"
    context_object_name = "movie"

class ProfileDetailView(DetailView):
    '''Display a single Profile.'''

    model = Profile
    template_name = "project/show_profile.html"
    context_object_name = "profile"

    def get_object(self):
        '''returns a Profile object either by primary key
        or by the logged in user'''
        if 'pk' in self.kwargs:
            return Profile.objects.get(pk=self.kwargs['pk'])
        if self.request.user.is_authenticated:
            return Profile.objects.get(user=self.request.user)
        return None

class UpdateProfileView(ProfileLoginMixin, UpdateView):
    '''View class to handle update of an profile based on its PK.'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = "project/update_profile_form.html"

    def get_object(self):
        '''returns the Profile of the logged in user.'''
        return self.get_current_profile()

class CreateProfileView(CreateView):
    '''A view to handle the creation of a new Profile.'''

    form_class = CreateProfileForm
    template_name = "project/create_profile_form.html"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
        context = super().get_context_data(**kwargs)

        # add the UserCreationForm to the context dictionary
        if self.request.method == 'POST':
            context['user_form'] = UserCreationForm(self.request.POST)
        else:
            context['user_form'] = UserCreationForm()
        return context
    
    def form_valid(self, form):
        '''This method handles the form submission and saves the 
        new object to the Django database.
        We need to add the foreign key (of the Profile) to the Post
        object before saving it to the database.
        '''

        # reconstruct the UserCreationForm instance
        user_form = UserCreationForm(self.request.POST)

        if user_form.is_valid():
            # save the user
            user = user_form.save()
            # log the user in
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            # attach this user to the profile
            form.instance.user = user
            return super().form_valid(form)  # saves post via superclass
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        '''Return the URL to redirect to after creating a new Profile.'''
    
        return reverse('show_profile', kwargs={'pk': self.object.pk})

class CreateReviewView(ProfileLoginMixin, CreateView):
    '''A view to handle creation of a new review on an Profile.'''
 
    form_class = CreateReviewForm
    template_name = "project/create_review_form.html"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
 
        # calling the superclass method
        context = super().get_context_data()
 
        # get the movie being reviewed
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        context['movie'] = movie
        context['profile'] = self.get_current_profile()
        return context
 
    def form_valid(self, form):
        '''This method handles the form submission and saves the 
        new object to the Django database.
        We need to add the foreign key (of the Profile) to the Review
        object before saving it to the database.
        '''
        
        print(form.cleaned_data)
        # get the profile of the logged in user
        profile = self.get_current_profile()
        # get the movie being reviewed
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        # attach this profile to the post
        form.instance.profile = profile # set the FK
        form.instance.movie = movie
        return super().form_valid(form) # saves post via superclass

    def get_success_url(self):
        '''Return the URL to redirect to after creating a new Review.'''
        pk = self.kwargs['pk']
        # redirect to the profile page
        return reverse('show_movie', kwargs={'pk': pk})

class UpdateReviewView(ProfileLoginMixin, UpdateView):
    '''View class to handle update of an Review based on its PK.'''

    model = Review
    form_class = UpdateReviewForm
    template_name = "project/update_review_form.html"

    def get_success_url(self):
        '''Return the URL to redirect to after updating a Review.'''
        review = self.get_object()
        return reverse('show_movie', kwargs={'pk': review.movie.pk})

class DeleteReviewView(ProfileLoginMixin, DeleteView):
    '''View class to delete a review on a profile.'''

    model = Review
    template_name = "project/delete_review_form.html"

    def get_success_url(self):
        '''Return the URL to redirect to after a successful delete.'''
 
        # find the PK for this Review:
        pk = self.kwargs['pk']
        # find the Review object:
        review = Review.objects.get(pk=pk)

        # return the URL to redirect to:
        return reverse('show_movie', kwargs={'pk': review.movie.pk})

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
 
        # calling the superclass method
        context = super().get_context_data(**kwargs)
 
 
        # find/add the review to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        review = Review.objects.get(pk=pk)
 
 
        # add this review and profile into the context dictionary:
        context['review'] = review
        context['movie'] = review.movie
        return context

class ShowFollowersDetailView(DetailView):
    '''Display a Profiles follower list.'''

    model = Profile
    template_name = "project/show_followers.html"
    context_object_name = "profile"

class ShowFollowingDetailView(DetailView):
    '''Display which Profiles a specific Profile is following.'''

    model = Profile
    template_name = "project/show_following.html"
    context_object_name = "profile"

class ShowFeedView(ProfileLoginMixin, DetailView):
    '''Display the review feed for a specific profile based on their following.'''

    model = Profile
    template_name = "project/show_feed.html"
    context_object_name = "profile"

    def get_object(self):
        '''returns the Profile of the logged in user.'''
        return self.get_current_profile()

class FollowProfileView(ProfileLoginMixin, TemplateView):
    '''View to handle following a person's Profile.'''

    template_name = "project/show_profile.html"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request to follow a profile.'''
        follower_profile = self.get_current_profile()
        # find which profile to follow
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        # create their follow
        Follow.objects.create(profile=profile, follower_profile=follower_profile)

        # redirect to the profile page
        return redirect(reverse('show_profile', kwargs={'pk': profile.pk}))

class UnfollowProfileView(ProfileLoginMixin, TemplateView):
    '''View to handle unfollowing a person's Profile.'''

    template_name = "project/show_profile.html"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request to unfollow a profile.'''
        follower_profile = self.get_current_profile()
        # find which profile to unfollow
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        # delete their follow
        Follow.objects.filter(profile=profile, follower_profile=follower_profile).delete()

        # redirect to the profile page
        return redirect(reverse('show_profile', kwargs={'pk': profile.pk}))

class LikeReviewView(ProfileLoginMixin, TemplateView):
    '''View to handle liking a Review.'''
    
    template_name = "project/show_movie.html"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request to like a review.'''
        profile = self.get_current_profile()
        # find which review to like
        pk = self.kwargs['pk']
        review = Review.objects.get(pk=pk)

        # add the like to the review
        Like.objects.create(review=review, profile=profile)

        # redirect to the review page
        return redirect(reverse('show_movie', kwargs={'pk': review.movie.pk}))

class UnlikeReviewView(ProfileLoginMixin, TemplateView): 
    '''View to handle unliking a Review.'''

    template_name = "project/show_movie.html"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request to unlike a review.'''
        profile = self.get_current_profile()
        # find which review to unlike
        pk = self.kwargs['pk']
        review = Review.objects.get(pk=pk)

        # remove the like from the review
        Like.objects.filter(review=review, profile=profile).delete()

        # redirect to the review page
        return redirect(reverse('show_movie', kwargs={'pk': review.movie.pk}))

class AddToWatchlistView(ProfileLoginMixin, TemplateView):
    '''View to handle adding a Movie to a Profile's Watchlist.'''

    template_name = "project/show_movie.html"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request to add a movie to the watchlist.'''
        profile = self.get_current_profile()
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        Watchlist.objects.create(movie=movie, profile=profile)
        return redirect(reverse('show_movie', kwargs={'pk': movie.pk}))

class RemoveFromWatchlistView(ProfileLoginMixin, TemplateView):
    '''View to handle removing a Movie from a Profile's Watchlist.'''

    template_name = "project/show_movie.html"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request to remove a movie from the watchlist.'''
        profile = self.get_current_profile()
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        Watchlist.objects.filter(movie=movie, profile=profile).delete()
        return redirect(reverse('show_movie', kwargs={'pk': movie.pk}))

class SearchView(ProfileLoginMixin, ListView):
    '''Handles the searching of Profiles and Movies.'''

    model = Movie
    template_name = "project/search_results.html"
    context_object_name = "movies"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request, but if no query is provided then return the search form.'''
        if 'query' not in request.GET:
            # check to see if the user is logged in
            if not request.user.is_authenticated:
                return redirect(self.get_login_url())
            # find the profile of the logged in user
            profile = self.get_current_profile()
            # return the search form template
            return render(request, 'project/search.html', {'profile': profile})
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        '''Returns movies that match the search query.'''
        query = self.request.GET.get('query', '')
        # reference: https://www.w3schools.com/django/ref_lookups_icontains.php
        movies = Movie.objects.filter(title__icontains=query) 
        return movies

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''

        # calling the superclass method
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')

        # get the profile of the logged in user
        profile = self.get_current_profile()


        # add profile, query (if any), posts (that match the query), profiles (that match the query) into the context dictionary:
        context['profile'] = profile
        context['query'] = query
        # reference: https://www.w3schools.com/django/ref_lookups_icontains.php
        context['movies'] = (Movie.objects.filter(title__icontains=query) | 
                            Movie.objects.filter(director__icontains=query) |  
                            Movie.objects.filter(genre__icontains=query))
        context['profiles'] = (Profile.objects.filter(username__icontains=query) |   
                               Profile.objects.filter(display_name__icontains=query))
        return context

