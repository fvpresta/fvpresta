# coding=utf8

from settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT_PATH = 'D:/www/Django-Projects/fvpresta';

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'fvpresta',                      # Or path to database file if using sqlite3.
        'USER': 'fvpresta',                      # Not used with sqlite3.
        'PASSWORD': 'hahaha',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TEMPLATE_DIRS = (
    PROJECT_ROOT_PATH + '/templates',
)

STATICFILES_DIRS = (
    PROJECT_ROOT_PATH + '/static',
)


MEDIA_ROOT = PROJECT_ROOT_PATH + '/media' # Example: "/home/media/media.lawrence.com/media/"
MEDIA_URL = '/media/' # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
STATIC_ROOT = '' # Example: "/home/media/media.lawrence.com/static/"
STATIC_URL = '/static/' # Example: "http://media.lawrence.com/static/"
