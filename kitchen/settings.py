SECRET_KEY = 'anything-secret'
DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'urls'
INSTALLED_APPS = []
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': False,
    'OPTIONS': {'context_processors': []},
}]