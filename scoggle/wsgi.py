"""
WSGI config for scoggle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scoggle.settings")

application = get_wsgi_application()

if os.environ.get('DJANGO_SECRET_KEY'):
	from whitenoise.django import DjangoWhiteNoise
	
	# Serve the static file with Django WhiteNoise package
	application = DjangoWhiteNoise(application)