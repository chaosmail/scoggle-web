from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^settings/account$', views.settings_account, name='settings-account'),
    url(r'^settings/keys$', views.settings_keys, name='settings-keys'),
    url(r'^(?P<username>[\w-]+)$', views.user, name='user'),
    url(r'^(?P<username>[\w-]+)/(?P<project_slug>[\w-]+)$', views.project, name='project'),
]