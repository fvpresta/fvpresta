__author__ = 'hthieu1110'
# coding=utf8

from settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'C:/Users/th.ha/www/django-projects/fvpresta/db/fvpresta.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TEMPLATE_DIRS = (
    'C:/Users/th.ha/www/django-projects/fvpresta/templates',
)

STATICFILES_DIRS = (
    'C:/Users/th.ha/www/django-projects/fvpresta/static',
)


MEDIA_ROOT = '' # Example: "/home/media/media.lawrence.com/media/"
MEDIA_URL = '' # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
STATIC_ROOT = '' # Example: "/home/media/media.lawrence.com/static/"
STATIC_URL = '/static/' # Example: "http://media.lawrence.com/static/"
