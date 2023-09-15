from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Setting an environment variable for project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'change_currencies.settings')

# Instantiating a Celery Object
app = Celery('change_currencies')

# Loading settings from a Django file
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically detect and register tasks from tasks.py files in Django applications
app.autodiscover_tasks()