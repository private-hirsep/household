import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["hirsep.pythonanywhere.com"]

def get_env_variable(var_name):
    value = os.environ.get(var_name)
    if value is None:
        raise Exception(f"Missing required environment variable: {var_name}")
    return value

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.production.sqlite3',
    }
}