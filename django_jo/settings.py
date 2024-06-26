"""
Django settings for django_jo project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url
import django_heroku
from decouple import config
#import environ

#env = environ.Env()
#environ.Env.read_env()
SECRET_KEY='django-insecure-5ftc@ot()mju46$sw5h#ar_d^3oe8=ym^3nky@uj=^9pe^$%5y'
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

#ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
#ALLOWED_HOSTS = ['localhost','127.0.0.1','examen222-dfbc0e25d483.herokuapp.com','examm-fiverr-037f3e5b5715.herokuapp.com']
AUTH_USER_MODEL = 'user.UserProfile'
#ALLOWED_HOSTS = ['*'] 
ALLOWED_HOSTS = ['*','bloc3exam-a2922cc2f685.herokuapp.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'user',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_extensions',
    'offer',
    'purchase',
    'whitenoise.runserver_nostatic', 
  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_jo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       
        'DIRS': [os.path.join(BASE_DIR, 'frontend')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',  
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        #'rest_framework.authentication.TokenAuthentication',
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=40),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

WSGI_APPLICATION = 'django_jo.wsgi.application'

# DATABASES = {
#     'default': dj_database_url.config(default=config('DATABASE_URL'))
# }
# if 'DYNO' in os.environ:
#     DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}
#else:
    #DATABASES['default']['OPTIONS'] = {'sslmode': 'disable'}


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'd6o59a1vr7apit',
    #     'USER': 'u368vaaq04pve0',
    #     'PASSWORD': 'p90608fb7ca023c9d96b62ada42424823c71276389b6c36398c075db634402a44',
    #     'HOST': 'ce0lkuo944ch99.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',
    #     'PORT': '5432',
    #      'OPTIONS': {
    #         'sslmode': 'require',
    #     },
    # }



       'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'USER': 'ubs9h052rggt2m',
         'PASSWORD': 'p459fc3862d6dc15e569eaa3e264768d034d1f3ce5e301706a25e97087f0d1ee0',
         'HOST': 'c7u1tn6bvvsodf.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com',
         'PORT': '5432',
         'NAME': 'd412olpe262c9o',
     }
}



if DEBUG:
    DATABASES["default"]={
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'AdminStudi',
        'PASSWORD': 'Bloc3exam2024',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'NAME': 'jeux_studi'

    }
else:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'))



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

CORS_ALLOWED_ORIGINS = [ 
    'https://bloc3exam-a2922cc2f685.herokuapp.com',  
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'frontend/static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

SSL_CRT_FILE = config('SSL_CRT_FILE', default=None)
SSL_KEY_FILE = config('SSL_KEY_FILE', default=None)
HTTPS = config('HTTPS', default=False, cast=bool)

# Configure Django App for Heroku.
django_heroku.settings(locals())

