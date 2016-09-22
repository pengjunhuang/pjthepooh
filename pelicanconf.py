#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'PJ'
SITENAME = u'PJ the Pooh'
SITEURL = ''

# SITENAME = u'PJ the Pooh'
# SITESUBTITLE = u'Enjoy the little things in life'
SITE_LICENSE = u'PJ the Pooh 2016'

## Paths
PATH = 'content'
NOTEBOOK_DIR = 'notebooks'
# STATIC_PATHS = ['images']
# ARTICLE_PATHS = ['images']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


USE_FOLDER_AS_CATEGORY = False

### User Defined

# Theme
THEME = 'pelican-elegant'

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Post
MARKUP = ['md']

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''


# Home Page
LANDING_PAGE_ABOUT = {'title': 'Enjoy the little things in life',

                      'details':
                          """
                          I'm currently a data scientist working in Uber Technologies Inc.
                          """}
