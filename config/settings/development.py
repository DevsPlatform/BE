"""
Development settings for DevsPlatform project.
"""

from .base import *
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Development Apps
INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

# Development Middleware
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# Database - Override for development if needed
# Uses SQLite for quick development setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# To use PostgreSQL in development, uncomment below and comment SQLite above
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME', default='devsplatform_dev'),
#         'USER': config('DB_USER', default='postgres'),
#         'PASSWORD': config('DB_PASSWORD', default='postgres'),
#         'HOST': config('DB_HOST', default='localhost'),
#         'PORT': config('DB_PORT', default='5432'),
#     }
# }

# Cache Configuration - Use dummy cache for development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# To use Redis in development, uncomment below
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': config('REDIS_URL', default='redis://localhost:6379/0'),
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

# CORS Settings for development
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Django Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

# Email Backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable S3 in development
USE_S3 = False

# Static and Media files for development
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Logging - More verbose for development
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['apps']['level'] = 'DEBUG'

# Create logs directory if it doesn't exist
import os
logs_dir = BASE_DIR / 'logs'
if not logs_dir.exists():
    logs_dir.mkdir()

# Django Extensions
SHELL_PLUS_PRINT_SQL = True

# Development-specific settings
CELERY_TASK_ALWAYS_EAGER = True  # Run tasks synchronously in development
CELERY_TASK_EAGER_PROPAGATES = True

# REST Framework settings for development
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += [
    'rest_framework.renderers.BrowsableAPIRenderer',
]

# Disable password validation in development for easier testing
AUTH_PASSWORD_VALIDATORS = []