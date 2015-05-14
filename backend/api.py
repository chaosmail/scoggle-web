from rest_framework import generics, permissions
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


class ProjectList(generics.ListCreateAPIView):
    """
    API endpoint that lists all projects or creates new projects
    """
    model = Project
    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        This view should return a list of all the projects
        for the currently authenticated user.
        """
        user = self.request.user

        # Filter by Slug
        slug = self.request.QUERY_PARAMS.get('slug', None)
        if slug is not None:
            return Project.objects.filter(owner=user, slug=slug).order_by('-edited_at')

        return Project.objects.filter(owner=user).order_by('-edited_at')

    def perform_create(self, serializer):
        """Force owner to the current user on save"""
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that shows project details, updates and deletes it
    """
    model = Project
    serializer_class = ProjectSerializer
    lookup_field = 'project_id'

    def get_queryset(self):
        """
        This view should return a list of all the projects
        for the currently authenticated user.
        """
        user = self.request.user
        return Project.objects.filter(owner=user)


class RunList(generics.ListCreateAPIView):
    """
    API endpoint that lists all runs or creates new runs
    """
    model = Run
    serializer_class = RunSerializer

    def get_queryset(self):
        """
        This view should return a list of all the runs
        for the current project.
        """
        if not "project_id" in self.request.GET:
            return []

        user = self.request.user
        project_id = self.request.GET["project_id"]
        project = Project.objects.get(project_id=project_id, owner=user)

        if not project:
            return []

        # Filter by Slug
        slug = self.request.QUERY_PARAMS.get('slug', None)
        if slug is not None:
            return Run.objects.filter(project=project, slug=slug).order_by('-edited_at')

        return Run.objects.filter(project=project).order_by('-edited_at')

    def perform_create(self, serializer):
        """Force project to the current project on save"""
        
        if not "project_id" in self.request.GET:
            raise ValueError("Need to define project_id")
        
        user = self.request.user
        project_id = self.request.GET["project_id"]
        project = Project.objects.get(project_id=project_id, owner=user)

        serializer.save(project=project)


class RunDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that shows run details, updates and deletes it
    """
    model = Run
    serializer_class = RunSerializer
    lookup_field = 'run_id'

    def get_queryset(self):
        """
        This view should return a list of all the runs
        for the current project.
        """
        user = self.request.user

        return Run.objects.filter(project__owner=user)


class ScoreList(generics.ListCreateAPIView):
    """
    API endpoint that lists all scores or creates new scores
    """
    model = Score
    serializer_class = ScoreSerializer

    def get_queryset(self):
        """
        This view should return a list of all the scores
        for the current project.
        """
        user = self.request.user
        
        if "project_id" in self.request.GET:
            
            project_id = self.request.GET["project_id"]
            project = Project.objects.get(project_id=project_id, owner=user)

            if not project:
                return []

            runs = Run.objects.filter(project=project)

            return Score.objects.filter(run__in=runs).order_by('-created_at')

        elif "run_id" in self.request.GET:
            
            run_id = self.request.GET["run_id"]
            run = Run.objects.get(run_id=run_id)

            if not run:
                return []

            if run.project.owner != user:
                raise ValueError("No permissions to load scores from this run")

            return Score.objects.filter(run=run).order_by('-created_at')

        else:

            runs = Run.objects.filter(project__owner=user)

            return Score.objects.filter(run__in=runs).order_by('-created_at')

    def perform_create(self, serializer):
        """Force project to the current project on save"""
        
        user = self.request.user

        if "project_id" in self.request.GET:
            project_id = self.request.GET["project_id"]
            project = Project.objects.get(project_id=project_id)

            if project.owner != user:
                raise ValueError("No permissions to store scores to this project")

        elif "run_id" in self.request.GET:
            run_id = self.request.GET["run_id"]
            run = Run.objects.get(run_id=run_id)

            if run.project.owner != user:
                raise ValueError("No permissions to store scores to this run")

            serializer.save(run=run)


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that shows run details, updates and deletes it
    """
    model = Score
    serializer_class = ScoreSerializer
    lookup_field = 'score_id'

    def get_queryset(self):
        """
        This view should return a list of all the runs
        for the current project.
        """
        user = self.request.user

        return Scenario.objects.filter(project__owner=user)