from rest_framework.authtoken.models import Token

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

from backend.models import *

def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required
def user(request, username):

    # TODO: make permissions
    if username != request.user.username:
        raise Http404("You need to login to view this profile!")

    try:
        token = Token.objects.get(user=request.user)
    except Token.DoesNotExist:
        token = None

    context = {'token': token}
    return render(request, 'user.html', context)

@login_required
def project(request, username, project_slug):

    # TODO: make permissions
    if username != request.user.username:
        raise Http404("You need to login to view this profile!")

    project = Project.objects.get(slug=project_slug, owner=request.user)
    
    try:
        token = Token.objects.get(user=request.user)
    except Token.DoesNotExist:
        token = None

    context = {'project': project, 'token': token}
    return render(request, 'project.html', context)

@login_required
def settings(request):
    return redirect('settings-profile')

@login_required
def settings_profile(request):
    context = {}
    return render(request, 'settings/profile.html', context)

@login_required
def settings_keys(request):
    try:
        token = Token.objects.get(user=request.user)
    except Token.DoesNotExist:
        token = None

    context = {'token': token}
    return render(request, 'settings/keys.html', context)