#!/usr/bin/env python
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *  # noqa


SITEURL = 'https://blog.mattlebrun.com'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

# URL Settings
# See: http://docs.getpelican.com/en/stable/settings.html#url-settings
DRAFT_URL = ''
DRAFT_SAVE_AS = ''
DRAFT_LANG_URL = ''
DRAFT_LANG_SAVE_AS = ''

# Feed Settings
FEED_ALL_ATOM = 'feeds/blog.mattlebrun.com.all.atom.xml'
FEED_ALL_RSS = 'feeds/blog.mattlebrun.com.all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/blog.mattlebrun.com.{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/blog.mattlebrun.com.{slug}.rss.xml'
TAG_FEED_ATOM = 'feeds/blog.mattlebrun.com.{slug}.atom.xml'
TAG_FEED_RSS = 'feeds/blog.mattlebrun.com.{slug}.rss.xml'

# Theme Settings
# GOOGLE_ANALYTICS = None
