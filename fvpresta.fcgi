#!/usr/bin/python2.7
import sys, os

# For import django
sys.path.insert(0, "/home/hthieu/www/pro/django-projects/virtualenvs/fvpresta/lib/python2.7/site-packages")

# Switch to the directory of your project.
os.chdir("/home/hthieu/www/pro/django-projects/fvpresta/")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings.prod"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
