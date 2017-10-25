#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = 'https://blog.mattlebrun.com'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True


# Feed Settings
FEED_ALL_ATOM = 'feeds/blog.mattlebrun.com.all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/blog.mattlebrun.com.%s.atom.xml'


# Custom Template Settings
GOOGLE_ANALYTICS = 'UA-9679489-4'