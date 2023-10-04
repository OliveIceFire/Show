"""
WSGI config for show project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
# Add your project's directory the PYTHONPATH
# path = '/home/rangodemo2020/tango_with_django_project/'
path = '/home/ForShow/app/'

if path not in sys.path:
    sys.path.append(path)
# Move to the project directory
os.chdir(path)
# Tell Django where the settings.py module is located

# Set up Django -- let it instantiate everything!
import django
django.setup()
# Import the Django WSGI to handle requests
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'show.settings')

application = get_wsgi_application()
