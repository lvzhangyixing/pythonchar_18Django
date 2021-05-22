"""
WSGI config for python实践char_18Django入门 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python实践char_18Django入门.settings')

application = get_wsgi_application()

application = Cling(get_wsgi_application())
