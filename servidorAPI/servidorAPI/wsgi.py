"""
WSGI config for servidorAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

sys.path = ['/var/www/', '/usr/lib/python2.7'] + sys.path
os.environ["DJANGO_SETTINGS_MODULE"] = "servidorAPI.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
