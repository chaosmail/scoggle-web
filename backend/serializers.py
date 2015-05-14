from rest_framework import serializers

from django.contrib.auth.models import User, Group

from .helpers.serializers import JSONSerializerField
from .models import *


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    
    params = JSONSerializerField()

    class Meta:
        model = Score
        fields = ('created_at', 'score', 'duration', 'params', 'is_valid' )


class RunSerializer(serializers.HyperlinkedModelSerializer):

    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Run
        fields = ('run_id', 'created_at', 'edited_at', 'name', 'description', 'slug', 'scores', 'color' )


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Project
        fields = ('project_id', 'created_at', 'edited_at', 'name', 'description', 'slug', 'url')
