from django.conf.urls import include, url

from . import views
from .api import *

urlpatterns = [
    
    # Authentication
    url(r'^auth/login/$', views.auth_login, name="api-auth-login"),
    url(r'^auth/logout/$', views.auth_logout, name="api-auth-logout"),
    url(r'^auth/signup/$', views.auth_signup, name="api-auth-signup"),

    # API Project Urls
    url(r'^project/(?P<project_id>[\w-]+)/$', ProjectDetail.as_view(), name='api-project-detail'),
    url(r'^project/$', ProjectList.as_view(), name='api-education-list'),
    
    # API Run Urls
    url(r'^run/(?P<run_id>[\w-]+)/$', RunDetail.as_view(), name='api-run-detail'),
    url(r'^run/$', RunList.as_view(), name='api-run-list'),

    # API Score Urls
    url(r'^score/(?P<score_id>[\w-]+)/$', ScoreDetail.as_view(), name='api-score-detail'),
    url(r'^score/$', ScoreList.as_view(), name='api-score-list'),
]