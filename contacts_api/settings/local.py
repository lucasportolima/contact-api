"""
Django settings for contacts_api project local.
"""
from .base import *
import sys


ALLOWED_HOSTS = ["*"]

if os.getenv("ALLOWED_HOSTS"):
    ALLOWED_HOSTS = json.loads(os.getenv("ALLOWED_HOSTS"))

DEBUG = True

# debug_toolbar settings
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

# ENABLING CORS
# https://pypi.org/project/django-cors-headers/
INSTALLED_APPS.append('corsheaders')
MIDDLEWARE.insert(2, 'corsheaders.middleware.CorsMiddleware')
CORS_ORIGIN_ALLOW_ALL = True

"""
Django settings for contacts_api project using envfile
Available on compose/docker/envfile

Please check all variables and set as you want
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("MACAPA_DB_NAME"),
        'USER': os.getenv("MACAPA_DB_USER"),
        'PASSWORD': os.getenv("MACAPA_DB_PASSWORD"),
        'HOST': os.getenv("MACAPA_DB_HOST"),
        'PORT': os.getenv("MACAPA_DB_PORT"),
        'TEST': {
            'MIRROR': 'default',
        }
    },
    'macapa': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("VAREJAO_DB_NAME"),
        'USER': os.getenv("VAREJAO_DB_USER"),
        'PASSWORD': os.getenv("VAREJAO_DB_PASSWORD"),
        'HOST': os.getenv("VAREJAO_DB_HOST"),
        'PORT': os.getenv("VAREJAO_DB_PORT"),
        'TEST': {
            'MIRROR': 'default',
        }
    }
}

DATABASE_ROUTERS = [
    'macapa.dbrouters.MacapaRouter',
    'varejao.dbrouters.VarejaoRouter',
]

VAREJAO_CONNECTION_STRING_ENGINE = f"postgresql://{'admin'}:{'admin'}@{'postgresql'}/{'admin'}"

MACAPA_CONNECTION_STRING_ENGINE = f"mysql://{'admin'}:{'admin'}@{'mysql'}/{'admin'}"
