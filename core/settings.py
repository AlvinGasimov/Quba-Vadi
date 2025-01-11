from pathlib import Path
import os
from os import getenv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@%9xl-!3gj1j4@cy0#4o8e_ah00jsd17cne2ngl=0gfa=vf2&4'
# SECRET_KEY = getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'room.apps.RoomConfig',
    'service.apps.ServiceConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'user.apps.UserConfig',
    'rosetta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# if not DEBUG:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': getenv('POSTGRES_DB'),
#             'USER': getenv('POSTGRES_USER'),
#             'PASSWORD': getenv('POSTGRES_PASSWORD'),
#             'HOST': getenv('POSTGRES_HOST'),
#             'PORT': 5432,
#         }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'az'

USE_TZ = True

USE_L10N = True

USE_I18N = True

TIME_ZONE = 'UTC'

LANGUAGES = (
    ('en', 'English'),
    ('az', 'Azerbaijan'),
    ('ru', 'Russian'),
    ('ar', 'Arabic'),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'az'
MODELTRANSLATION_LANGUAGES = ('en', 'az', 'ru', 'ar')

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CSRF_TRUSTED_ORIGINS = []