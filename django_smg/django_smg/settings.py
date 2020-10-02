import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False

# load secrets and frequently changed values from config.json
if DEBUG:
    with open(os.path.join(BASE_DIR, 'django_smg', 'dev_config.json'), 'r') as jsn:
        config = json.load(jsn)
else:
    with open(os.path.join(BASE_DIR, 'django_smg', 'config.json'), 'r') as jsn:
        config = json.load(jsn)

SECRET_KEY = config['DJANGO_SECRET']
ALLOWED_HOSTS = [
    'songmakergallery.com',
    'ec2-18-220-82-134.us-east-2.compute.amazonaws.com',
    'localhost',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_mysql',
    'knox',
    'storages',
    'rest_framework',

    'accounts',
    'get_screenshots',
    'frontend',
    'public_provider',
    'teacher_admin',
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

ROOT_URLCONF = 'django_smg.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'knox.auth.TokenAuthentication',
    )
}

CRON_CLASSES = [
    'get_screenshots.api.ScreenshotCron',
]

# Email
EMAIL_PORT = 587
EMAIL_HOST_USER = config['SMG_GMAIL']
EMAIL_HOST_PASSWORD = config['SMG_GMAIL_PASSWORD']
EMAIL_USE_TLS = True
EMAIL_HOST = config['SMTP_HOST']
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Amazon S3
if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = config['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = config['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = config['AWS_STORAGE_BUCKET_NAME']
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_FILE_OVERWRITE = True
# default file storage config
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'django_smg', 'templates')
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

WSGI_APPLICATION = 'django_smg.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'songmaker',
        'USER': config['MYSQL_USER'],
        'PASSWORD': config['MYSQL_USER_PASS'],
        'HOST': 'db',
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode=\"STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO\""
        },
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_ci',
        }
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file_logger': {
            'level': 0,
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'main.log'),
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file_logger'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'loggers': {
        'file': {
            'handlers': ['file_logger'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}