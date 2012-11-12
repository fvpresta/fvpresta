__author__ = 'hthieu1110'
# coding=utf8

from settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT_PATH = '/home/hthieu/www/pro/django-projects/fvpresta'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hthieu_fvpresta',                      # Or path to database file if using sqlite3.
        'USER': 'hthieu_fvpresta',                      # Not used with sqlite3.
        'PASSWORD': 'fvpresta',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TEMPLATE_DIRS = (
    PROJECT_ROOT_PATH + '/templates',
)

# STATICFILES_DIRS should not contain STATIC_ROOT
STATICFILES_DIRS = (
    PROJECT_ROOT_PATH + '/static',
)
STATIC_ROOT = '' # Serves when using collecstatic
STATIC_URL = '/static/'

MEDIA_ROOT = PROJECT_ROOT_PATH + '/media'
MEDIA_URL = '/media/'
