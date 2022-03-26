from .common import *
from .partials.utils import get_secret


###############
# ENVIRONMENT #
###############

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')
PUBLIC_KEY = get_secret('PUBLIC_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_secret('DEBUG')

ALLOWED_HOSTS = list(get_secret('ALLOWED_HOSTS'))


def show_toolbar(request):
    """
    The default callback checks if the IP is internal, but docker's IP
    addresses are not in INTERNAL_IPS, so we force the display in dev mode
    :param request: The intercepted request
    :return: True OR False
    """
    return get_secret('DEBUG_TOOLBAR') == "True"


DEV_APPS = [
    'corsheaders',
    'debug_toolbar',
]

INSTALLED_APPS = INSTALLED_APPS + DEV_APPS

DEV_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE = MIDDLEWARE + DEV_MIDDLEWARE  # CORS middleware should be at the top of the list

CORS_ALLOW_ALL_ORIGINS = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    'SKIP_TEMPLATE_PREFIXES': (
        'django/forms/widgets/',
        'admin/widgets/',
        'menus/',
        'pipeline/',
    ),
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

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
