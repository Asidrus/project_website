import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv('.env')
ENV_LOCAL = './.env_local'
if os.path.isfile(ENV_LOCAL):
    load_dotenv(ENV_LOCAL)

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') is not None

BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = [BASE_DIR / "website/static"]
STATIC_ROOT = BASE_DIR / "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = ''
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ROOT_URLCONF = 'website.urls'
WSGI_APPLICATION = 'website.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ALLOWED_HOSTS = ["*"]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'order.apps.OrderConfig'
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'apps/order/static/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": os.environ.get("DB_DATABASE", BASE_DIR / "db.sqlite3"),
#         "USER": os.environ.get("DB_USER", "user"),
#         "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
#         "HOST": os.environ.get("DB_HOST", "localhost"),
#         "PORT": os.environ.get("DB_PORT", "5432"),
#     }
# }

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

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
