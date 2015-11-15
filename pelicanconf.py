#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gzlug'
SITENAME = u'GZLug'
SITEURL = ''
BANNER_SUBTITLE = '广州Linux用户组'

PATH = 'content'

TIMEZONE = u'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Site Source', 'https://github.com/fangpeishi/gzlug.org/'),
         ('Slides', 'https://github.com/gzlug/slides'),
	 ('Techparty', 'http://techparty.org/'))

# Social widget
SOCIAL = (('GitHub','https://github.com/gzlug'),
	  ('Twitter','https://twitter.com/GuangzhouLUG'),
          ('GoogleGroup', 'https://groups.google.com/forum/#!forum/gzlug'),
          ('Weibo', 'http://weibo.com/gzlug'),
          ('Douban', 'http://www.douban.com/people/gzlug/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'pelican-themes/pelican-bootstrap3'
