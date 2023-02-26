"""
Django settings for devx project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#q)tvq((i9rqs=gar)wkk19+dqlqqj8mf%x-0cz3fd(g=3jzrt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition


INSTALLED_APPS = [
    # 'jazzmin',
    'admin_tools_stats',  # this must be BEFORE 'admin_tools' and 'django.contrib.admin'
    'django_nvd3',
    'admin_soft.apps.AdminSoftDashboardConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
    'corsheaders',
    'mail'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
import os
ROOT_URLCONF = 'devx.urls'
ADMIN_CHARTS_NVD3_JS_PATH = 'bow/nvd3/build/nv.d3.js'
ADMIN_CHARTS_NVD3_CSS_PATH = 'bow/nvd3/build/nv.d3.css'
ADMIN_CHARTS_D3_JS_PATH = 'bow/d3/d3.js'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.custom_context.site_globals'
            ],
        },
    },
]

WSGI_APPLICATION = 'devx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
else:

    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.postgresql',
        #     'NAME': 'postgres',
        #     'USER': 'postgres',
        #     'HOST': 'fdaa:1:762a:0:1::2',
        #     'PASSWORD':'lKjC6F6L2exs9UG',
        #     'PORT':5433
        #     # 'PORT': '3306'


        # }
        'default': dj_database_url.config(
            default="postgres://devx:E8ijkHOICHzP6Ba@[fdaa:1:762a:0:1::2]:5432/devx"
        )
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static/')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ALLOWED_ORIGINS=['https://devx.fly.dev/']
CORS_ALLOW_ALL_ORIGINS=True
CSRF_TRUSTED_ORIGINS = ['https://*.fly.dev']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gdsctiu@gmail.com'
# EMAIL_HOST_PASSWORD = 'Rownak@10'
EMAIL_HOST_PASSWORD = 'gcomgbxcybxzjpak'