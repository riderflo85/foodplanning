from .default import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.14', '192.168.1.36']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'foodplanning_db',
#     'USER': os.environ.get('USER_DB'),
#     'PASSWORD': os.environ.get('PWD_DB'),
#     'HOST': os.environ.get('HOST_DB'),
#     'PORT': os.environ.get('PORT_DB'),
#     }
# }

# For local database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'foodplanning_db',
    'USER': 'florent',
    'PASSWORD': os.environ.get('PWDDB_LOCAL'),
    'HOST': '',
    'PORT': os.environ.get('PORT_DB'),
    }
}

# celery config
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'