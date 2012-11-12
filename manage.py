#!/usr/bin/env python2.7
import os
import sys

lib_path = "/home/hthieu/www/pro/django-projects/virtualenvs/fvpresta/lib/python2.7/site-packages"
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.prod")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
