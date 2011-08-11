import os
import djcelery
djcelery.setup_loader()

# Django settings for project.
DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
     ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

SERVER_EMAIL = 'newfies@localhost.com'

APPLICATION_DIR = os.path.dirname(globals()['__file__'])

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2','postgresql','mysql','sqlite3','oracle'
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': APPLICATION_DIR + '/database/test.db',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost.
                                         # Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default.
                                         # Not used with sqlite3.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = APPLICATION_DIR + "/static/"

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(APPLICATION_DIR, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = 'http://0.0.0.0:8000/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(APPLICATION_DIR, "resources"),
    ("newfies", os.path.join(APPLICATION_DIR, "resources")),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ujau$^uei_ak=@-v8va(&@q_sc0^1nn*qpwyc-776n&qoam@+v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'sentry.client.middleware.SentryResponseErrorIdMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'common.filter_persist_middleware.FilterPersistMiddleware',
    #'sentry.client.middleware.Sentry404CatchMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APPLICATION_DIR, 'templates'),
)
INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS = (
    #admin tool apps
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.markup',
    'countries',
    'prefix_country',
    'dialer_gateway',
    'dialer_campaign',
    'dialer_cdr',
    #'dialer_cdr.api',
    'dialer_settings',
    'user_profile',
    'common',
    'djcelery',
    'django_extensions',
    'dateutil',
    'pagination',
    'memcache_status',
    'notification',
    'voip_app',
    'sentry',
    'sentry.client',
    #'debug_toolbar',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'dilla',
    #'test_extensions',
)
AUTH_PROFILE_MODULE = "user_profile.UserProfile"
LOGIN_URL = '/pleaselog/'


#DILLA SETTINGS
#==============
DICTIONARY = "/usr/share/dict/words"
DILLA_USE_LOREM_IPSUM = False  # set to True ignores dictionary
DILLA_APPS = [
                'auth',
                #'dialer_gateway',
                'voip_app',
                'dialer_campaign',
                'dialer_cdr',
             ]
DILLA_SPAMLIBS = [
                #'voip_app.voip_app_custom_spamlib',
                #'dialer_campaign.dialer_campaign_custom_spamlib',
                 'dialer_cdr.dialer_cdr_custom_spamlib',
                ]
# To use Dilla
# > python manage.py run_dilla --cycles=100


#MEMCACHE
#========
CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    'LOCATION': '127.0.0.1:11211',
    'KEY_PREFIX': 'newfies_',
  }
}

#CELERY SETTINGS
#===============
CARROT_BACKEND = 'ghettoq.taproot.Redis'
#CARROT_BACKEND = 'redis'

BROKER_HOST = 'localhost'  # Maps to redis host.
BROKER_PORT = 6379         # Maps to redis port.
BROKER_VHOST = 0        # Maps to database number.


CELERY_RESULT_BACKEND = 'redis'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
#REDIS_CONNECT_RETRY = True

"""
from datetime import timedelta
from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    "runs-every-second": {
        "task": "dialer_campaign.tasks.campaign_running",
        "schedule": timedelta(seconds=1),
        #"args": (50)
    },
}
"""

#LANGUAGES
#===========
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    #('fr', gettext('French')),
    #('es', gettext('Spanish')),
    #('br', gettext('Brazilian')),
)

#DJANGO-ADMIN-TOOL
#=================
ADMIN_TOOLS_MENU = 'custom_admin_tools.menu.CustomMenu'

ADMIN_TOOLS_INDEX_DASHBOARD =\
'custom_admin_tools.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD =\
'custom_admin_tools.dashboard.CustomAppIndexDashboard'

#PISTON
#======
PISTON_DISPLAY_ERRORS = True
PISTON_EMAIL_ERRORS = "root@localhost.localdomain"
#PISTON_IGNORE_DUPE_MODELS = True

# Use only in Debug mode. Not in production
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

#PLIVO
#=====
PLIVO_DEFAULT_ANSWER_URL = 'http://127.0.0.1:8000/api/dialer_cdr/answercall/'
PLIVO_DEFAULT_HANGUP_URL = 'http://127.0.0.1:8000/api/dialer_cdr/hangupcall/'

# ADD 'dummy','plivo','twilio'
NEWFIES_DIALER_ENGINE = 'plivo'

API_ALLOWED_IP = ['127.0.0.1', 'localhost']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/newfies/newfies-django.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'myapp': {
            'handlers': ['logfile'],
            'level': 'WARNING',  # Or maybe INFO or DEBUG
            'propogate': False
        },
    },
}


#IMPORT LOCAL SETTINGS
#=====================
from settings_local import *

