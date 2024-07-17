from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "user.User"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # internal apps 
    'user.apps.UserConfig',
    'authentication.apps.AuthenticationConfig',
    'mood.apps.MoodConfig',
    'artist.apps.ArtistConfig',
    'album.apps.AlbumConfig',
    'genre.apps.GenreConfig',
    'playlist.apps.PlaylistConfig',
    'track.apps.TrackConfig',
    # external apps 
    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        'DIRS': [
            BASE_DIR / "templates"
            ],
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

WSGI_APPLICATION = 'core.wsgi.application'

# rest framework config
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS" : "drf_spectacular.openapi.AutoSchema" , 
    "DEFAULT_AUTHENTICATION_CLASSES" : [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

# JWT config 
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME" : timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME" : timedelta(hours=3),
}

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# drf spectacular config

SPECTACULAR_SETTINGS = {
    "TITLE" : "BACKEND-SONGSARA",
    "VERSION" : "1.0.0",
    "DESCRIPTION" : "API of songsara built with django rest framework ."
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# email config

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 465 
EMAIL_USE_SSL = True

# celery config 
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL","redis://localhost:6379/")
CELERY_BACKEND_URL = os.environ.get("CELERY_BACKEND_URL","redis://localhost:6379/")

# static files 
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# media files 
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "media/"