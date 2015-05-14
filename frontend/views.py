from rest_framework.authtoken.models import Token

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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

    token = Token.objects.get(user=request.user)

    context = {'token': token}
    return render(request, 'user.html', context)

@login_required
def project(request, username, project_slug):

    # TODO: make permissions
    if username != request.user.username:
        raise Http404("You need to login to view this profile!")

    project = Project.objects.get(slug=project_slug, owner=request.user)
    token = Token.objects.get(user=request.user)

    context = {'project': project, 'token': token}
    return render(request, 'project.html', context)