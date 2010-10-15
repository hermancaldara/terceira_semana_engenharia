# -*- coding: utf-8 -*-
# Django settings for terceira_semana_engenharia project.

import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Herman da Rosa Caldara', 'hermancaldara@gmail.com'),
    ('Vinícius das Chagas Silva', 'vinimaster@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(PROJECT_ROOT_PATH, 'terceira_semana_engenharia.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'site_media')

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/site_media'

# URL prefix for admin media -- CSS, JavaScript and images.
ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = '@ho0z=44l1my7*1l6&ko-*g1=gbc^hghre&+38+2k6zixbjemr'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'terceira_semana_engenharia.urls'

TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT_PATH, 'templates'),
	os.path.join(PROJECT_ROOT_PATH, 'subscribe/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'subscribe',
	'news',
)
