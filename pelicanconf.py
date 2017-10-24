#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Matt Lebrun'
SITENAME = 'Matt Lebrun'
SITESUBTITLE = 'in between code, coffee, and peanut butter.'
SITEURL = 'http://localhost:8000'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = (25)
DEFAULT_PAGINATION = 5

TIMEZONE = 'Asia/Manila'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 5
RELATIVE_URLS = True


# URL Settings
# See: http://docs.getpelican.com/en/stable/settings.html#url-settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'

DRAFT_URL = 'draft/{slug}.html'
DRAFT_SAVE_AS = 'draft/{slug}.html'
DRAFT_LANG_URL = 'draft/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'draft/{slug}-{lang}.html'

PAGE_URL = 'page/{slug}.html'
PAGE_SAVE_AS = 'page/{slug}.html'
PAGE_LANG_URL = 'page/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'page/{slug}-{lang}.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}.html'


# Path Settings
PATH = 'content'
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
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Link Settings
LINKS = (
    ('Home', SITEURL),
    ('Archives', '{}/archives.html'.format(SITEURL)),
    ('About', 'https://mattlebrun.com'),
)

SOCIAL = (
    ('Github', 'https://github.com/cr8ivecodesmith'),
    ('Twitter', 'https://twitter.com/cr8ivecodesmith'),
)


# Meta data Settings
DEFAULT_METADATA = {
    'status': 'draft',
    'category': 'uncategorized',
    'author': AUTHOR,
    # 'date': '{:%Y-%m-%d %H:%M}'.format(datetime.now()),
    # 'modified': '{:%Y-%m-%d %H:%M}'.format(datetime.now()),
}


# Custom Template Settings
COPYRIGHT_TEXT = '&copy; 2017 Matt Lebrun'
TWITTER_USERNAME = 'cr8ivecodesmith'
GOOGLE_ANALYTICS = None
