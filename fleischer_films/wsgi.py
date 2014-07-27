"""
WSGI config for fleischer_films project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fleischer_films.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
