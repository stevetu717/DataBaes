"""
Django settings for Databaes project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p@zh%^j=%v^1y%9#y=l2vu9&*l#+550j#w#(=2g7$=r(y%4ul='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'Crate',
    'account',
    'payment',
    'bootstrap3',
    'bootstrap_themes',
    'registration',
    "pinax.stripe"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'pinax.stripe.middleware.ActiveSubscriptionMiddleware',
]

ROOT_URLCONF = 'Databaes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ]
        ,
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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

WSGI_APPLICATION = 'Databaes.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use the recommended django mysql adapter
        'NAME': 'databaes',
        'USER': 'lqiu96',
        'PASSWORD': 'pennstate2018',
        'HOST': '108.16.36.150',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/static/media/'

# Django-registration-redux Variables
SITE_ID = 1
ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # Automatically log the user in.
LOGIN_URL = 'homepage'  # The page users are directed to if they are not logged in
# and are trying to access pages requiring authentication
LOGIN_REDIRECT_URL = 'homepage'  # The page you want users to arrive at after they successful log in
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Pinax Stripe Settings and Variables
PINAX_STRIPE_PUBLIC_KEY = 'pk_test_XCcdTdwGIrUPzSeAJ8ImmFcR'
PINAX_STRIPE_SECRET_KEY = 'sk_test_GmaJVY0Z32BsxeTeqHh41ij7'
#decide later
# PINAX_STRIPE_SUBSCRIPTION_REQUIRED_EXCEPTION_URLS = []
# PINAX_STRIPE_SUBSCRIPTION_REQUIRED_REDIRECT = Defaults to none
# PINAX_STRIPE_INVOICE_FROM_EMAIL

