from base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'https://theqablog.herokuapp.com/qa-paypal-sands/'
PAYPAL_RECEIVER_EMAIL = 'mncursebusiness@hotmail.com'

SITE_URL = 'https://theqablog.herokuapp.com'
ALLOWED_HOSTS.append('theqablog.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
