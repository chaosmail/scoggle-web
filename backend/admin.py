from django.contrib import admin

from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'owner', 'edited_at',)
    exclude = ('edited_at',)

@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    
    list_display = ('project', 'name', 'slug', 'edited_at',)
    exclude = ('edited_at',)

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    
    list_display = ('run', 'score', 'created_at',)