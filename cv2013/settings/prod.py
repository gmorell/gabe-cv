from .base import *

ALLOWED_HOSTS = ['.gmp.io','.gmp.pw','.gaaaaaaa.be','.gabrielmorell.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': env_var("DB_NAME"),                      # Or path to database file if using sqlite3.
        'USER': env_var("DB_USER"),                      # Not used with sqlite3.
        'PASSWORD': env_var("DB_PASS"),                  # Not used with sqlite3.
        'HOST': env_var("DB_HOST", "localhost"),                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': env_var("DB_PORT", 5432),                      # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = env_var("DJ_SECRET_KEY")

MEDIA_ROOT = env_var("DJ_APP_ROOT") + "/www/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = env_var("DJ_APP_ROOT") + "/www/static/"
STATIC_URL = '/static/'

PDF_HEADER = env_var("PDF_HEADER")
PDF_CONTACT = env_var("PDF_CONTACT")

import os
import raven
RAVEN_CONFIG = {
    'dsn': env_var("RAVEN_DSN"),
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}


GA_TRACKING_ID = env_var("DJ_GA_ID")

SITE_URL = env_var("DJ_SITE_URL")

DEBUG=False
