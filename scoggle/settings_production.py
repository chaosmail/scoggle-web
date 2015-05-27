import os

# Import the common Settings
from settings import *

"""Place all production settings here"""
import dj_database_url

# Disable debugging in production
DEBUG = False

# Read the secret key from env var
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Allow heroku hosts
ALLOWED_HOSTS = [
	'.herokuapp.com'
]

# Set a root directory for the static files
STATIC_ROOT = "staticfiles"

# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Some Security Settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'