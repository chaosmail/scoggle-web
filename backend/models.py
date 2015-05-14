import uuid

import jsonfield

from django.db import models
from django.conf import settings
from django.utils import timezone

from .helpers.fields import AutoDateTimeField


class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    project_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    edited_at = AutoDateTimeField(default=timezone.now, editable=False)
    slug = models.SlugField(max_length=50, default="")
    url = models.URLField(max_length=200, default="")
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


class Run(models.Model):
    project = models.ForeignKey(Project, related_name='runs')
    run_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    edited_at = AutoDateTimeField(default=timezone.now, editable=False)
    slug = models.SlugField(max_length=50, default="")
    color = models.CharField(max_length=50, default="steelblue")
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


class Score(models.Model):
    run = models.ForeignKey(Run, related_name='scores')
    score_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    is_valid = models.BooleanField(default=True, blank=True)
    score = models.DecimalField(default=0.0, max_digits=20, decimal_places=12)
    duration = models.DecimalField(default=0.0, max_digits=14, decimal_places=6, blank=True)
    params = jsonfield.JSONField(default={}, blank=True)

    def __str__(self):
        return str(self.score)