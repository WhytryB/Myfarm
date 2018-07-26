import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangopeo',
        'USER': 'postgres',
        'PASSWORD': 'Robinzon68',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True