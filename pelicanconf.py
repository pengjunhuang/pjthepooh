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
SOCIAL = (('Email', 'mailto:huangpj1110@gmail.com'),
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
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'pelican-toc']

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


SITE_LICENSE = u'&copy; PJ the Pooh 2016'

# Home Page
LANDING_PAGE_ABOUT = {'title': 'Enjoy the little things in life',

                      'details':
                          """
                          <p>
                          My name is PJ, born and raised in <a href="https://en.wikipedia.org/wiki/Guangzhou"> Guangzhou, China</a>. I'm currently a <a href="https://en.wikipedia.org/wiki/Data_science">data scientist</a> in <a href="(https://en.wikipedia.org/wiki/Silicon_Valley">Silicon Valley</a>, immersing myself in a world of science and new technology. I truly believe that most great decisions are driven by data. I'm willing to learn as much as I can to become a full-stack data scientist.</p>

                          <p>
                          I love sports such as swimming, basketball, snowboarding and bicycling. To be a better version of myself, I love to travel! My another big interest is teaching. I believe that sharing knowledge takes a key role in human society.
                          </p>

                          <p>
                          As a first-generation immigrant in U.S., I would love to contribute my little effort to help the <a href="https://en.wikipedia.org/wiki/History_of_Chinese_Americans">Chinese immigrant</a> community.
                          </p>

                          <p>
                          I speak Cantonese, Mandarin and English.
                          </p>
                          """}

TOC = {
    'TOC_HEADERS'       : '^h[1-6]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'false',     # If 'true' include title in toc
}