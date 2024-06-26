"""
Django settings for fruit_store project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g2((+x6$0k2y#-vjg4l)y2g64n5n7lv^x99r^=i%cdkt@a9+&_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
SITE_ID = 5

INSTALLED_APPS = [
    # all suth for social login like google
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'fs_app',
    'authentication',
    'products',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # for social login add middleware
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'fruit_store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # `allauth` needs this from django
                'django.template.context_processors.request',
                
                #custom context processro added for viewing cart items on all pages 
                'fs_app.context_processors.cart_items',
                
                'fs_app.context_processors.cart_items',
            ],
        },
    },
]

WSGI_APPLICATION = 'fruit_store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_project_db',
        'USER': 'root',
        'PASSWORD': 'Suprit@6788',
        'HOST': 'localhost',   
        'PORT': '3306',
    }
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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_DIR = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = '/static/'

# media fils configurations

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# In your settings.py file

AUTH_USER_MODEL = 'authentication.User'


# AUTHENTICATION BACKEND for all auth social login
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # 'EMAIL_AUTHENTICATION': True,
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    }
}

SOCIALACCOUNT_LOGIN_ON_GET = True



LOGIN_URL = '/authentication/login'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = '/'

# Set to True if email is required for social accounts
SOCIALACCOUNT_EMAIL_REQUIRED = True


SESSION_COOKIE_SECURE = True  # Ensure this is True if serving over HTTPS
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'authentication.pipeline.save_profile_image',  
)


# Razorpay Payment integration

RAZORPAY_KEY_ID = 'rzp_test_zsghZMWlkKoLnR'
RAZORPAY_KEY_SECRET = 'ohuqBE0dpa0AhLx6Ed3hMiaN'
