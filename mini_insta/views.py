# File: views.py
# Author: Emily Vespasiano (evespa@bu.edu), 6/2/2026
# Description: View classes for the mini_insta app. Displays
# all mini_insta profiles and individual profile pages.
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Profile, Post, Photo, Follow, Like
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm, CreateProfileForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin ## for authentication
from django.contrib.auth.forms import UserCreationForm ## for new User
from django.contrib.auth import login
from datetime import date 

# Create your views here.
class ProfileLoginMixin(LoginRequiredMixin):
    '''Mixin class that handles login requirements for views classes.'''

    def get_login_url(self):
        '''return the URL for this app's login page'''
        return reverse('login')

    def get_current_profile(self):
        '''return the current profile user logged in'''
        return Profile.objects.get(user=self.request.user)



class ProfileListView(ListView):
    '''Define a view class to show all mini_insta Profiles.'''

    model = Profile
    template_name = "mini_insta/show_all_profiles.html"

    # plural variable named to hold all profile objects to be displayed in the template
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    '''Display a single mini_insta profile.'''

    model = Profile
    template_name = "mini_insta/show_profile.html"
    # singular 'profile' so that you can access the object in the template
    context_object_name = "profile" 

    def get_object(self):
        '''returns a Profile object either by primary key
        or by the logged in user'''
        if 'pk' in self.kwargs:
            return Profile.objects.get(pk=self.kwargs['pk'])
        if self.request.user.is_authenticated:
            return Profile.objects.get(user=self.request.user)
        return None

class PostDetailView(DetailView):
    '''Display a single post.'''
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
        context = super().get_context_data(**kwargs)
        # add the profile to context for the bottom nav
        if self.request.user.is_authenticated:
            context['profile'] = Profile.objects.get(user=self.request.user)
        else:
            # use the post's profile for the nav (if logged out)
            context['profile'] = self.get_object().profile
        return context

class CreatePostView(ProfileLoginMixin, CreateView):
    '''A view to handle creation of a new post on an Profile.'''
 
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_context_data(self):
        '''Return the dictionary of context variables for use in the template.'''
 
        # calling the superclass method
        context = super().get_context_data()
 
 
        # get the profile of the logged in user
        profile = self.get_current_profile()
 
 
        # add this profile into the context dictionary:
        context['profile'] = profile
        return context
 
    def form_valid(self, form):
        '''This method handles the form submission and saves the 
        new object to the Django database.
        We need to add the foreign key (of the Profile) to the Post
        object before saving it to the database.
        '''
        
        print(form.cleaned_data)
        # get the profile of the logged in user
        profile = self.get_current_profile()
        # attach this profile to the post
        form.instance.profile = profile # set the FK
        response = super().form_valid(form) # saves post via superclass

        # handles file uploads for photos
        files = self.request.FILES.getlist('files')
        for file in files:
            Photo.objects.create(post=self.object, image_file=file)

        return response

    def get_success_url(self):
        '''Return the URL to redirect to after creating a new Post.'''
        # get the profile of the logged in user
        profile = self.get_current_profile()

        # redirect to the profile page
        return reverse('show_profile', kwargs={'pk': profile.pk})

class UpdateProfileView(ProfileLoginMixin, UpdateView):
    '''View class to handle update of an profile based on its PK.'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"

    def get_object(self):
        '''returns the Profile of the logged in user.'''
        return self.get_current_profile()

class DeletePostView(ProfileLoginMixin, DeleteView):
    '''View class to delete a post on a profile.'''

    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_success_url(self):
        '''Return the URL to redirect to after a successful delete.'''
 
        # find the PK for this Comment:
        pk = self.kwargs['pk']
        # find the Comment object:
        post = Post.objects.get(pk=pk)
        
        # find the PK of the Profile to which this post is associated:
        profile = post.profile
        
        # return the URL to redirect to:
        return reverse('show_profile', kwargs={'pk':profile.pk})

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
 
        # calling the superclass method
        context = super().get_context_data(**kwargs)
 
 
        # find/add the article to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
 
 
        # add this post and profile into the context dictionary:
        context['post'] = post
        context['profile'] = post.profile
        return context

class UpdatePostView(ProfileLoginMixin, UpdateView):
    '''View class to handle update of an post based on its PK.'''

    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_context_data(self, **kwargs):
        '''Return the dictionary of context variables for use in the template.'''
 
        # calling the superclass method
        context = super().get_context_data(**kwargs)
 
 
        # find/add the article to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
 
 
        # add this postinto the context dictionary:
        context['post'] = post
        return context

class ShowFollowersDetailView(DetailView):
    '''Display a Profiles follower list.'''

    model = Profile
    template_name = "mini_insta/show_followers.html"
    context_object_name = "profile"

class ShowFollowingDetailView(DetailView):
    '''Display which Profiles a specific Profile is following.'''

    model = Profile
    template_name = "mini_insta/show_following.html"
    context_object_name = "profile"

class ShowFeedView(ProfileLoginMixin, DetailView):
    '''Display the post feed for a specific profile based on their following.'''

    model = Profile
    template_name = "mini_insta/show_feed.html"
    context_object_name = "profile"

    def get_object(self):
        '''returns the Profile of the logged in user.'''
        return self.get_current_profile()

class SearchView(ProfileLoginMixin, ListView):
    '''Handles the searching of Profiles and Posts.'''

    model = Post
    template_name = "mini_insta/search_results.html"
    context_object_name = "posts"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request, but if no query is provided then return the search form.'''
        if 'query' not in request.GET:
            # check to see if the user is logged in
            if not request.user.is_authenticated:
                return redirect(self.get_login_url())
            # find the profile of the logged in user
            profile = self.get_current_profile()
            # return the search form template
            return render(request, 'mini_insta/search.html', {'profile': profile})
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        '''Returns posts that match the search query.'''
        query = self.request.GET.get('query', '')
        # reference: https://www.w3schools.com/django/ref_lookups_icontains.php
        posts = Post.objects.filter(caption__icontains=query) 
        return posts

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
        context['posts'] = Post.objects.filter(caption__icontains=query) 
        context['profiles'] = (Profile.objects.filter(username__icontains=query) |  
                               Profile.objects.filter(display_name__icontains=query) |  
                               Profile.objects.filter(bio_text__icontains=query))
        return context

class CreateProfileView(CreateView):
    '''A view to handle the creation of a new Profile.'''

    form_class = CreateProfileForm
    template_name = "mini_insta/create_profile_form.html"

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
            # set the join date to current day
            form.instance.join_date = date.today()
            # attach this user to the profile
            form.instance.user = user
            return super().form_valid(form)  # saves post via superclass
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        '''Return the URL to redirect to after creating a new Profile.'''
    
        return reverse('show_profile', kwargs={'pk': self.object.pk})

class FollowProfileView(ProfileLoginMixin, TemplateView):
    '''View to handle following a person's Profile.'''

    template_name = "mini_insta/show_profile.html"

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

    template_name = "mini_insta/show_profile.html"

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

class LikePostView(ProfileLoginMixin, TemplateView):
    '''View to handle liking a Post.'''
    
    template_name = "mini_insta/show_profile.html"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request to like a post.'''
        profile = self.get_current_profile()
        # find which post to like
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        # add the like to the post
        Like.objects.create(post=post, profile=profile)

        # redirect to the post page
        return redirect(reverse('show_post', kwargs={'pk': post.pk}))

class UnlikePostView(ProfileLoginMixin, TemplateView): 
    '''View to handle unliking a Post.'''

    template_name = "mini_insta/show_profile.html"

    def dispatch(self, request, *args, **kwargs):
        '''Dispatch the request to unlike a post.'''
        profile = self.get_current_profile()
        # find which post to unlike
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)

        # remove the like from the post
        Like.objects.filter(post=post, profile=profile).delete()

        # redirect to the post page
        return redirect(reverse('show_post', kwargs={'pk': post.pk}))