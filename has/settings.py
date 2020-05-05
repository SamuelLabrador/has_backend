"""
Django settings for has project.
Generated by 'django-admin startproject' using Django 2.2.9.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# Try to import secret key
try:
    from .secret_key import SECRET_KEY
except ImportError:
    key = get_random_secret_key()
    
    SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(SETTINGS_DIR, 'secret_key.py')
    
    f = open(path, "w")
    f.write("SECRET_KEY = '{}'".format(key))
    f.close()
    from .secret_key import SECRET_KEY


if 'HAS_PRODUCTION' in os.environ:
    PRODUCTION_FLAG = bool(int(os.environ['HAS_PRODUCTION']))
else: 
    PRODUCTION_FLAG = False

if 'PIPELINE_FLAG' in os.environ:
    PIPELINE_FLAG = bool(os.environ['PIPELINE_FLAG'])

print('PRODUCTION: ', PRODUCTION_FLAG)
# SECURITY WARNING: don't run with debug turned on in production!
if PRODUCTION_FLAG:
    DEBUG = False
    ALLOWED_HOSTS = [
        '.highwayanalytics.us',
    ]
else:
    DEBUG = True
    ALLOWED_HOSTS = ['*']

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures')
]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'restapp',
    'cctv',
    'corsheaders',
]

if PIPELINE_FLAG:
    INSTALLED_APPS += 'datapipeline'


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'has.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'has.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


if PRODUCTION_FLAG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD' : os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': 5432,
        }
    }
    CACHES = {
	    'default': {
	        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
	        'LOCATION': 'cache:11211',
	    }
	}

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    CACHES = {
    	'default': {
        	'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    	}
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

VALID_COUNTIES = [
    'Riverside',
    'San Bernardino',
]

# SESSION CONFIGURATION
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# CORS Configuration
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'OPTIONS',
    'PUT',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
ML_MODEL_ROOT = os.path.join(BASE_DIR, 'ml_models')

STATIC_ROOT = '/static/'
STATIC_URL = os.path.join(BASE_DIR, 'static/')

print(STATIC_ROOT)
print(STATIC_URL)

IMAGE_ROOT = os.path.join(STATIC_ROOT, 'cctv_images')
IMAGE_URL = os.path.join(STATIC_URL, 'cctv_images')

