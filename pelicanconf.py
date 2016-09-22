#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'PJ'
SITENAME = u'PJ the Pooh'
SITEURL = 'http://localhost:8000'
DISQUS_SITENAME = 'pjthepooh'

# SITENAME = u'PJ the Pooh'
# SITESUBTITLE = u'Enjoy the little things in life'


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
SOCIAL = (('Email', 'mailto:pjthepooh@gmail.com'),
          ('Linkedin', 'https://www.linkedin.com/in/pjhuang'),
          ('Facebook', 'https://www.facebook.com/peejay1110')
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


USE_FOLDER_AS_CATEGORY = False

### User Defined

# Theme
THEME = 'pelican-elegant'

# Plugins and extensions
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Elegant theme
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Elegant Labels
COMMENTS_INTRO = u'Leave your comments below.'
RELATED_POSTS_LABEL = 'Keep Reading'
SOCIAL_PROFILE_LABEL = u'Keep in Touch'
SHARE_POST_INTRO = u'Share on:'


# Mailchimp
# EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
# EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
# SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
# MAILCHIMP_FORM_ACTION = u'empty'



EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Post
MARKUP = ['md']


MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']


SITE_LICENSE = u'&copy; PJ the Pooh 2016 '

# Home Page
LANDING_PAGE_ABOUT = {'title': 'Enjoy the little things in life',

                      'details':
                          """
                          I'm currently a data scientist working in Uber Technologies Inc.
                          """}

