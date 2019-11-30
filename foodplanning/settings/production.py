import os
from .default import *


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME_DB'),
        'USER': os.environ.get('USER_DB'),
        'PASSWORD': os.environ.get('PWD_DB'),
        'HOST': os.environ.get('HOST_DB'),
        'PORT': os.environ.get('PORT_DB'),
    }
}

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

# celery config
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
