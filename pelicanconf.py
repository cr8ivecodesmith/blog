#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))

AUTHOR = 'Matt Lebrun'
SITENAME = 'matt lebrun'
SITESUBTITLE = 'in between code, coffee, and peanut butter.'
SITEURL = 'http://localhost:8000'
SUMMARY_MAX_LENGTH = 25

TIMEZONE = 'Asia/Manila'
DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

RELATIVE_URLS = True

# URL Settings
# See: http://docs.getpelican.com/en/stable/settings.html#url-settings
# NOTE:
# Referencing static content must be relative from the slug pattern.
# i.e. if images is in `static/images` and slug is `year/month/slug.html`,
# image references should be `../../static/images/image.jpg`
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'

PAGE_URL = 'page/{slug}.html'
PAGE_SAVE_AS = 'page/{slug}.html'
PAGE_LANG_URL = 'page/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'page/{slug}-{lang}.html'

DRAFT_URL = ''
DRAFT_SAVE_AS = ''
DRAFT_LANG_URL = ''
DRAFT_LANG_SAVE_AS = ''

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}.html'
# MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%B}.html'
MONTH_ARCHIVE_SAVE_AS = ''
# DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%B}/{date:%d}.html'
DAY_ARCHIVE_SAVE_AS = ''


# Path Settings
PATH = os.path.join(BASEDIR, 'content')
STATIC_PATHS = [
    'static/images',
    'static/downloads',

    'static/extras/CNAME',
    'static/extras/robots.txt',
]
EXTRA_PATH_METADATA = {
    'static/extras/CNAME': {
        'path': 'CNAME',
    },
    'static/extras/robots.txt': {
        'path': 'robots.txt',
    },
}


# Ignore files Settings
IGNORE_FILES = [
    '__pycache__',
    '*.pid',
    '*.so',
    '*.tmp',
    '*.swp~',
    '*.swp',
    '.#*',
]


# Feed Settings
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

FEED_ATOM = None
FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None


# Link Settings
LINKS = (
    ('about', 'https://mattlebrun.com'),
)

SOCIAL = (
    ('github', 'https://github.com/cr8ivecodesmith'),
    ('twitter', 'https://twitter.com/cr8ivecodesmith'),
    # ('facebook', 'https://www.facebook.com/cr8ivecodesmith'),
    # ('instagram', 'https://instagram.com/cr8ivecodesmith'),
    ('linkedin', 'https://ph.linkedin.com/in/cr8ivecodesmith'),
)


# Meta data Settings
DEFAULT_METADATA = {
    'status': 'draft',
    'category': 'uncategorized',
    'author': AUTHOR,
    # 'date': '{:%Y-%m-%d %H:%M}'.format(datetime.now()),
    # 'modified': '{:%Y-%m-%d %H:%M}'.format(datetime.now()),
}


# Theme Settings
THEME = 'zenmatt'
PYGMENTS_STYLE = 'default'
COPYRIGHT_YEAR = '2021'
COPYLEFT = True
# GOOGLE_ANALYTICS = None
