from rest_framework.authtoken.models import Token

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def auth_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                
                # Log user in
                login(request, user)
                
                # Redirect to user's page
                return redirect('user', username=user.username)
            else:
                # TODO: Translate
                messages.error(request, "Your account is not activated!")
        else:
            # TODO: Translate
            messages.error(request, "The username or password is invalid!")
    
    return redirect('index')

def auth_logout(request):
    
    logout(request)

    # TODO: Translate
    messages.success(request, "You logged out successfully!")
    
    return redirect('index')

def auth_signup(request):

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not password:
            # TODO: Translate
            messages.error(request, "Please provide a valid password!")
        
        elif password != password2:
            # TODO: Translate
            messages.error(request, "Passwords must match!")

        elif User.objects.filter(username=username).count() > 0:
            # TODO: Translate
            messages.error(request, "Username already exists!")

        else:
            # Create a user
            user = User.objects.create_user(username, email, password)
            
            # Save the user
            user.save()

            # Log user in
            user = authenticate(username=username, password=password)
            login(request, user)

            # Redirect to user's page
            return redirect('user', username=user.username)

    return redirect('index')

def auth_update_profile(request):

    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        request.user.email = email
        request.user.first_name = first_name
        request.user.last_name = last_name
            
        # Save the user
        request.user.save()

        # TODO: Translate
        messages.success(request, "Your profile was updated successfully!")

        # Redirect to user's profile settings
        return redirect('settings-profile')

    return redirect('index')

def auth_create_token(request):

    if request.user:

        try:
            token = Token.objects.get(user=request.user)
        except Token.DoesNotExist:
            token = None

        # If there is a token available, remove it
        if token:
            token.delete()

        # Generate a new token
        Token.objects.create(user=request.user)

        # TODO: Translate
        messages.success(request, "Your API key was created successfully!")

        # Redirect to user's key settings
        return redirect('settings-keys')

    return redirect('index')

def auth_remove_token(request):

    if request.user:

        try:
            token = Token.objects.get(user=request.user)
        except Token.DoesNotExist:
            token = None

        # If there is a token available, remove it
        if token:
            token.delete()

            # TODO: Translate
            messages.success(request, "Your API key was removed successfully!")

        # Redirect to user's key settings
        return redirect('settings-keys')

    return redirect('index')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)