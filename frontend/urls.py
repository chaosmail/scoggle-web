from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>[\w-]+)$', views.user, name='user'),
    url(r'^(?P<username>[\w-]+)/(?P<project_slug>[\w-]+)$', views.project, name='project'),
]