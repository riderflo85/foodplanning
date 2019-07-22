from .default import *
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'foodplanning_db',
    'USER': os.environ.get('USER_DB'),
    'PASSWORD': os.environ.get('PWD_DB'),
    'HOST': os.environ.get('HOST_DB'),
    'PORT': os.environ.get('PORT_DB'),
    }
}