import os

SECRET_KEY = '1234'

MIDDLEWARE_CLASSES = tuple()

WITH_WQDB = os.environ.get('WITH_WQDB', False)
if WITH_WQDB:
    WQ_APPS = (
        'wq.db.rest',
        'wq.db.rest.auth',
    )
else:
    WQ_APPS = tuple()

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'data_wizard',
) + WQ_APPS + (
    'tests.file_app',
    'tests.data_app',
    'tests.naturalkey_app',
    'tests.eav_app',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'data_wizard_test',
        'USER': 'postgres',
    }
}

ROOT_URLCONF = "tests.urls"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

CELERY_RESULT_BACKEND = BROKER_URL = 'redis://localhost/0'

if WITH_WQDB:
    from wq.db.default_settings import *  # noqa
