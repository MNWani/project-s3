from base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000/QA_blog/'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/qa-paypal-sands/'
PAYPAL_RECEIVER_EMAIL = 'mncursebusiness@hotmail.com'
