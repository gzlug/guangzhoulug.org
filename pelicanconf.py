#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gzlug'
SITENAME = u'广州 GNU/Linux 用户组'
SITEURL = ''
BANNER_SUBTITLE = '广州 GNU/Linux 用户组'


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
LINKS = (('Site Source', 'https://github.com/gzlug/gzlug.org/'),
         ('Slides', 'https://github.com/gzlug/slides'),
         ('北京 GNU/Linux 用户组', 'https://blug.sh/'),
         ('清华大学 TUNA 协会', 'https://tuna.moe/'),
         ('上海 Linux 用户组', 'https://shanghailug.github.io/'),
         ('Techparty', 'http://techparty.org/'))

# Social widget
SOCIAL = (('GitHub','https://github.com/gzlug'),
          ('Twitter','https://twitter.com/GuangzhouLUG'),
          ('Weibo', 'http://weibo.com/gzlug'),
          ('Google Group', 'https://groups.google.com/group/gzlug'),
          ('Douban', 'http://www.douban.com/people/gzlug/'))

MENUITEMS = (('关于我们', '/pages/AboutUs.html'),
             ('加入我们', '/pages/JoinUs.html'),
             ('邮件列表', '/pages/MailingList.html'),
             ('寻路指南', '/pages/TransferGuide.html'),
             ('捐赠', '/pages/Donation.html'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'pelican-themes/pelican-bootstrap3'
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU=True

# Plugin setting
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['pelican-bootstrapify']
