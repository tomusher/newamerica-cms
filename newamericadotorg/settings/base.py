"""
Django settings for newamericadotorg project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os

SECRET_KEY = os.getenv("SECRET_KEY")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

INSTALLED_APPS = [
    'corsheaders',
    'home',
    'search',
    'programs',
    'person',
    'book',
    'article',
    'blog',
    'event',
    'conference',
    'collection',
    'podcast',
    'report',
    'policy_paper',
    'brief',
    'press_release',
    'quoted',
    'survey',
    'issue',
    'weekly',
    'the_thread',
    'in_depth',
    'other_content',
    'storages',
    'rss_feed',
    'subscribe',
    'wagtailautocomplete',
    'multiselectfield',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.contrib.legacy.richtext',
    'wagtail',
    'wagtail.contrib.styleguide',
    'wagtail.contrib.table_block',
    'wagtail.contrib.frontend_cache',
    'wagtail.contrib.settings',

    'modelcluster',
    'compressor',
    'taggit',
    'wand',
    'willow',
    'anymail',
    'createsend',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'rest_framework',
    'wagtail_headless_preview',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',

    # Gzip/minify
    'django.middleware.gzip.GZipMiddleware',
    # Content security policy
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'newamericadotorg.urls'
HTML_MINIFY = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'generated-templates'),
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'newamericadotorg.settings.context_processors.debug',
                'newamericadotorg.settings.context_processors.program_data',
                'newamericadotorg.settings.context_processors.about_pages',
                'newamericadotorg.settings.context_processors.locations',
                'newamericadotorg.settings.context_processors.meta'
            ]
        },
    },
]

WSGI_APPLICATION = 'newamericadotorg.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}


# Django HTTP settings

# X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True
# X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if 'S3_BUCKET_NAME' in os.environ and os.environ['S3_BUCKET_NAME'] != 'local':
    MEDIA_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    S3_MEDIA_DOMAIN = '%s.s3.amazonaws.com' % MEDIA_BUCKET_NAME
    MEDIA_URL = "https://%s/" % S3_MEDIA_DOMAIN
else:
    MEDIA_URL = '/media/'


# Basic authentication settings
# These are settings to configure the third-party library:
# https://gitlab.com/tmkn/django-basic-auth-ip-whitelist
if os.getenv("BASIC_AUTH_ENABLED", "false").lower().strip() == "true":
    # Insert basic auth as a first middleware to be checked first, before
    # anything else.
    MIDDLEWARE.insert(0, "baipw.middleware.BasicAuthIPWhitelistMiddleware")

    # This is the credentials users will have to use to access the site.
    BASIC_AUTH_LOGIN = os.getenv("BASIC_AUTH_LOGIN", "newamerica")
    BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "")

    # This is the list of network IP addresses that are allowed in without
    # basic authentication check.
    BASIC_AUTH_WHITELISTED_IP_NETWORKS = os.getenv("BASIC_AUTH_WHITELISTED_IP_NETWORKS", "").split(",")

    # This is the list of hosts that website can be accessed without basic auth
    # check. This may be useful to e.g. white-list "llamasavers.com" but not
    # "llamasavers.production.torchbox.com".
    if "BASIC_AUTH_WHITELISTED_HTTP_HOSTS" in os.environ:
        BASIC_AUTH_WHITELISTED_HTTP_HOSTS = os.getenv(
            "BASIC_AUTH_WHITELISTED_HTTP_HOSTS"
        ).split(",")


# Wagtail settings

WAGTAIL_SITE_NAME = "newamericadotorg"

WAGTAILIMAGES_IMAGE_MODEL = 'home.CustomImage'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 200000

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
        'OPTIONS': {
            'features': [
                'bold',
                'italic',
                'pullquote',
                'na-blockquote',
                'h2',
                'h3',
                'h4',
                'h5',
                'ol',
                'ul',
                'hr',
                'embed',
                'link',
                'document-link',
                'image',
                'undo',
                'redo',
            ]
        }
    }
}

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'newamericadotorg.api.pagination.CustomPagination'
}

HEADLESS_PREVIEW_CLIENT_URLS = {
    'default': 'http://localhost:8000/h_preview',
    'newamerica.org': 'https://www.newamerica.org/h_preview',
    'staging.newamerica.org': 'https://staging.newamerica.org/h_preview',
    'newamericadotorg.herokuapp.com': 'https://newamericadotorg.herokuapp.com/h_preview',
    'na-staging.herokuapp.com': 'https://na-staging.herokuapp.com/h_preview',
    'na-develop.herokuapp.com': 'https://na-develop.herokuapp.com/h_preview',
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Slack API
SLACK_NOTIFICATIONS_WEBHOOK = os.getenv('SLACK_NOTIFICATIONS_WEBHOOK')
SLACK_NOTIFICATIONS_CHANNEL = os.getenv('SLACK_NOTIFICATIONS_CHANNEL')


# Content Security Policy
CSP_REPORT_ONLY = True
CSP_DEFAULT_SRC = ("'self'", 'https://*.newamerica.org')
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",  # Needed for Wagtail admin pages
    'https://*.newamerica.org',
    'https://analytics.twitter.com',
    'https://bam.nr-data.net',
    'https://cdnjs.cloudflare.com',
    'https://d1y8sb8igg2f8e.cloudfront.net',
    'https://d3fvh0lm0eshry.cloudfront.net',
    'https://js-agent.newrelic.com',
    'https://load.sumo.com',
    'https://na-data-projects.s3.amazonaws.com',
    'https://platform.twitter.com',
    'https://s3.amazonaws.com/datadotnewamerica/',
    'https://ssl.google-analytics.com',
    'https://static.ads-twitter.com',
    'https://www.google-analytics.com',
    'https://www.google.com/recaptcha/',
    'https://www.googletagmanager.com',
    'https://www.gstatic.com/recaptcha/',
    'https://www.youtube.com',
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",  # Needed for dynamic inline styles
    'https://fonts.googleapis.com',
)
CSP_IMG_SRC = (
    "'self'",
    'https://*.newamerica.org',
    'https://*.gravatar.com',
    'https://analytics.twitter.com',
    'https://api.mapbox.com',
    'https://bam.nr-data.net',
    'https://d1y8sb8igg2f8e.cloudfront.net',
    'https://d3fvh0lm0eshry.cloudfront.net',
    'https://i.ytimg.com', # Youtube
    'https://micro-cdn.sumo.com',
    'https://na-production.s3.amazonaws.com',
    'https://na-staging.s3.amazonaws.com',
    'https://s3-us-west-2.amazonaws.com/na-data-projects/',
    'https://s3.amazonaws.com/new-america-composer/',
    'https://syndication.twitter.com',
    'https://t.co',
    'https://tile.openstreetmap.org',
    'https://www.google-analytics.com',
    'https://www.googletagmanager.com',
    'https://www.gstatic.com',
    # Specific image
    'http://assets.motherjones.com/politics/2011/inequality-page25_actualdistribwithlegend.png',
)
CSP_FRAME_SRC = (
    "'self'",
    'https://*.newamerica.org',
    'https://datawrapper.dwcdn.net',
    'https://www.google.com',
    'https://www.googletagmanager.com',
    # Embeds
    'https://airtable.com',
    'https://art19.com',
    'https://d1y8sb8igg2f8e.cloudfront.net',
    'https://docs.google.com',
    'https://e.infogr.am',
    'https://embed-ssl.ted.com',
    'https://embed.podcasts.apple.com',
    'https://embed.ted.com',
    'https://livestream.com',
    'https://m.facebook.com',
    'https://m.youtube.com',
    'https://my.matterport.com',
    'https://new-america.jebbit.com',
    'https://newamerica-graphics.github.io',
    'https://opentechinstitute.github.io',
    'https://platform.twitter.com',
    'https://player.vimeo.com',
    'https://playlist.megaphone.fm',
    'https://public.tableau.com',
    'https://renderer.apester.com',
    'https://resourcewatch.org',
    'https://s3.amazonaws.com/newamericadotorg/',
    'https://syndication.twitter.com',
    'https://w.soundcloud.com',
    'https://www.facebook.com',
    'https://www.flickr.com',
    'https://www.instagram.com',
    'https://www.youtube.com',
)
CSP_CONNECT_SRC = (
    "'self'",
    'https://*.tiles.mapbox.com',
    'https://analytics.google.com',
    'https://api.mapbox.com',
    'https://bam-cell.nr-data.net',
    'https://bam.nr-data.net',
    'https://chart-studio.herokuapp.com',
    'https://d3fvh0lm0eshry.cloudfront.net',
    'https://na-data-projects.s3.amazonaws.com',
    'https://na-data-sheetsstorm.s3.us-west-2.amazonaws.com',
    'https://releases.wagtail.io',
    'https://s3-us-west-2.amazonaws.com/na-data-projects/',
    'https://stats.g.doubleclick.net',
    'https://sumo.com',
    'https://varying-degrees.herokuapp.com',
    'https://www.google-analytics.com',
)
CSP_FONT_SRC = (
    "'self'",
    'https://d3fvh0lm0eshry.cloudfront.net',
    'https://fonts.googleapis.com',
    'https://fonts.gstatic.com',
    'https://na-fonts.s3.amazonaws.com',
)

CSP_REPORT_URI = os.environ.get('CSP_REPORT_URI')
CSP_REPORT_PERCENTAGE = 0.05
