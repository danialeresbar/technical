import os

from .common import *
from .partials.utils import get_secret


PUBLIC_KEY = get_secret('PUBLIC_KEY')
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_secret('DEBUG')

ALLOWED_HOSTS = get_secret('ALLOWED_HOSTS')

############
# DATABASE #
############

if get_secret('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': get_secret('DATABASE_NAME'),
            'USER': get_secret('DATABASE_USER'),
            'PASSWORD': get_secret('DATABASE_PASSWORD'),
            'HOST': get_secret('DATABASE_HOST'),
            'PORT': get_secret('DATABASE_PORT'),
        }
    }

########
# CORS #
########

CORS_ALLOWED_ORIGINS = list(get_secret('CORS_ALLOWED_ORIGINS'))
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'instance',
    'access',
]
