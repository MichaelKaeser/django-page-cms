# -*- coding: utf-8 -*-

# Django settings for cms project.
from django import VERSION as DJANGO_VERSION
import os
PROJECT_DIR =  os.path.dirname(__file__)

TEST_PROJ = 'gerbi.testproj'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
USE_TZ = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

CACHE_BACKEND = 'locmem:///'

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

MEDIA_ROOT = STATIC_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'media', 'static')
STATIC_URL = MEDIA_URL + 'static/'

# Absolute path to the directory that holds gerbi media.
# GERBI_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'gerbi', 'media', 'gerbi')
# Absolute path to the directory that holds media.
ADMIN_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'admin_media')
ADMIN_MEDIA_PREFIX = '/admin_media/'


FIXTURE_DIRS = [os.path.join(PROJECT_DIR, 'fixtures')]

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*xq7m@)*f2awoj!spa0(jibsrz9%c0d=e(g)v*!17y(vx0ue_3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db'
    }
}


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "gerbi.context_processors.media",
    #"staticfiles.context_processors.static_url",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)

ROOT_URLCONF = TEST_PROJ + '.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

CACHE_BACKEND = "locmem:///?timeout=300&max_entries=6000"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    TEST_PROJ + '.documents',
    #'tagging',
    'gerbi',
    'mptt',
    #'staticfiles',
    #'tinymce',
    # disabled to make "setup.py test" to work properly
    #'south',

    # these 2 package don't create any dependecies
    'authority',
    # haystack change coverage score report by importing modules
    #'haystack',
)

GERBI_TINYMCE = False
#GERBI_TAGGING = True

GERBI_CONNECTED_MODELS = [{
    'model':TEST_PROJ + '.documents.models.Document',
    'form':TEST_PROJ + '.documents.models.DocumentForm',
    'options':{
            'extra': 3,
            'max_num': 10,
        },
},]

# Default language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# This is defined here as a do-nothing function because we can't import
# django.utils.translation -- that module depends on the settings.
gettext_noop = lambda s: s

# languages you want to translate into the CMS.
GERBI_LANGUAGES = (
    ('de', gettext_noop('German')),
    ('fr-ch', gettext_noop('Swiss french')),
    ('en-us', gettext_noop('US English')),
)

# You should add here all language you want to accept as valid client
# language. By default we copy the GERBI_LANGUAGES constant and add some other
# similar languages.
languages = list(GERBI_LANGUAGES)
languages.append(('fr-fr', gettext_noop('French')))
languages.append(('fr-be', gettext_noop('Belgium french')))
languages.append(('it-it', gettext_noop('Italian')))
LANGUAGES = languages

# This enable you to map a language(s) to another one, these languages should
# be in the LANGUAGES config
def language_mapping(lang):
    if lang.startswith('fr'):
        # serve swiss french for everyone
        return 'fr-ch'
    return lang

GERBI_LANGUAGE_MAPPING = language_mapping

GERBI_DEFAULT_TEMPLATE = 'gerbi/examples/index.html'

GERBI_TEMPLATES = (
    ('gerbi/examples/base.html', 'base'),
    ('gerbi/examples/index.html', 'index'),
    ('gerbi/examples/nice.html', 'nice one'),
    ('gerbi/examples/cool.html', 'cool one'),
    ('gerbi/examples/editor.html', 'raw editor'),
    ('gerbi/tests/untranslated.html', 'untranslated'),
)

GERBI_SANITIZE_USER_INPUT = True

GERBI_USE_SITE_ID = True

HAYSTACK_SITECONF = 'example.search_sites'
HAYSTACK_SEARCH_ENGINE = 'dummy'
#HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_DIR, 'whoosh_index')

COVERAGE_EXCLUDE_MODULES = (
    "gerbi.migrations.*",
    "gerbi.tests.*",
    "gerbi.urls",
    "gerbi.__init__",
    "gerbi.search_indexes",
    "gerbi.management.commands.*",
)

COVERAGE_HTML_REPORT = True
COVERAGE_BRANCH_COVERAGE = False

GERBI_ENABLE_TESTS = True

#TEST_RUNNER = 'example.test_runner.run_tests'

#here = os.path.abspath(os.path.dirname(__file__))
#NOSE_ARGS = [os.path.join(here, os.pardir, "gerbi", "tests"),
#            "--cover3-package=gerbi",
#            "--cover3-branch",
#            "--with-coverage3",
#            "--cover3-html",
#            "--cover3-exclude=%s" % ",".join(COVERAGE_EXCLUDE_MODULES)]

try:
    from local_settings import *
except ImportError:
    pass
