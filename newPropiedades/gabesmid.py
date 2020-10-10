#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

#from __future__ import unicode_literals

# import os
# import shutil

# from utils import get_inet_ips
# from utils import splash_custom_fingerprint
import random
from random import choice
#import time
#import ast, urllib2
import ast
import urllib.request 

from datetime import datetime, timedelta

# from urlparse import urljoin

# from scrapy.exceptions import IgnoreRequest

# from scrapy.downloadermiddlewares.retry import RetryMiddleware
# from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
from scrapy import signals
# from scrapy.extensions.httpcache import FilesystemCacheStorage
# from scrapy.utils.request import request_fingerprint
# from scrapy.utils.httpobj import urlparse_cached
from scrapy.utils.project import get_project_settings
# from scrapy.utils.response import response_status_message
# from six.moves import cPickle as pickle
# from w3lib.http import headers_raw_to_dict, headers_dict_to_raw
# from scrapy.http import Headers, Response
# from scrapy.responsetypes import responsetypes
# from scrapy.utils.python import to_bytes, to_unicode


# ############### requets.py
# import hashlib
# import weakref
# from six.moves.urllib.parse import urlunparse

# from w3lib.http import basic_auth_header
# from scrapy.utils.python import to_bytes, to_native_str

# from w3lib.url import canonicalize_url
# from scrapy.utils.httpobj import urlparse_cached


import logging

logger = logging.getLogger()

# SETTINGS
NEUKOLLN_SETTINGS_USER_AGENT_CHOICES = 'NEUKOLLN_USER_AGENT_CHOICES'

NEUKOLLN_META_REFRESH_CACHE_KEY = "neukolln_refresh_cache"
NEUKOLLN_META_REFRESH_CACHE_DEFAULT_VALUE = False

NEUKOLLN_META_BANNED_KEY = 'neukolln_banned'

# SPIDER
NEUKOLLN_SPIDER_ROTATE_IP_ONLY_ATTR = 'neukolln_rotate_ip_only'  # rotate ip ONLY
NEUKOLLN_SPIDER_ROTATE_UA_ONLY_ATTR = 'neukolln_rotate_ua_only'  # rotate user-agent ONLY
NEUKOLLN_SPIDER_ROTATE_IP_UA_ATTR = 'neukolln_rotate_ua_ip'  # rotate user-agent AND ip
NEUKOLLN_SPIDER_SMART_ROTATE_IP_ATTR = 'neukolln_smart_rotate_ip'

# Set of default user agent
# Define here a list you wanna use
# http://useragentstring.com/pages/useragentstring.php
# Or fake it: https://pypi.python.org/pypi/fake-useragent
NEUKOLLN_USER_AGENT_DEFAULT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (iPad; CPU OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.79 Mobile/14D27 Safari/602.1',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;  Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 OPR/34.0.2036.25',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/56.0.2924.76 Chrome/56.0.2924.76 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144',
    'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
]



class NeukollnBaseMiddleware(object):
    """Mandatory class to connect middleware when spider is open (signal)"""

    @classmethod
    def from_crawler(cls, crawler):
        o = cls()
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)  # <============== mandatory!!!
        return o


class LuminatiRotateIpAddressMiddleware(NeukollnBaseMiddleware):

    #super_proxy = socket.gethostbyname('zproxy.luminati.io')
    #url = "http://%s-country-de-session-%s:%s@" + super_proxy + ":%d"
    #url = "http://%s-%s:%s@162.243.254.181:%d"
    #url = "http://%s-session-%s:%s@162.243.254.181:%d"
    url = "http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d"
    port = 22225

    def __init__(self):
        # [INFO] Alert user
        logger.info("[LUMINATI_ROTATE_IP_MIDDLEWARE][__INIT__][NEUKOLLN] Hello from middleware")

        # Credentials
        self._username = ""
        self._password = ""
        self._sessions_stack = []
        self._session_requests_limit = 10
        self._session_failures_limit = 2

        self.debug = False

        # Set list of user agent
        self.user_agents = get_project_settings().get(NEUKOLLN_SETTINGS_USER_AGENT_CHOICES)
        if not self.user_agents:
            # [DEBUG] Alert user
            logger.debug("[LUMINATI_ROTATE_IP_MIDDLEWARE][__INIT__][NEUKOLLN] %s is not set in the settings so a "
                         "default list of user agents from the library will be used." % NEUKOLLN_SETTINGS_USER_AGENT_CHOICES)
            self.user_agents = NEUKOLLN_USER_AGENT_DEFAULT_LIST

    def spider_opened(self, spider):
        if hasattr(spider, 'luminati_username'):
            # INFO it has to be the full username such as "lum-customer-autobiz-zone-autobiz_test_case-country-de-session"
            self._username = spider.luminati_username
        else:
            raise Exception("[LUMINATI_ROTATE_IP_MIDDLEWARE][SPIDER_OPENED][NEUKOLLN] Missing username (spider configuration)")

        if hasattr(spider, 'luminati_password'):
            self._password = spider.luminati_password
        else:
            raise Exception("[LUMINATI_ROTATE_IP_MIDDLEWARE][SPIDER_OPENED][NEUKOLLN] Missing password (spider configuration)")

        if hasattr(spider, 'luminati_allow_debug'):
            self.debug = spider.luminati_allow_debug
            if self.debug:
                logger.info("[LUMINATI_ROTATE_IP_MIDDLEWARE][SPIDER_OPENED][NEUKOLLN] Allow debug")

    def process_request(self, request, spider):
        """Set the correct IP using the pool of Ips"""

        # Retrieve session_id if exists else random e.g. reset session each time: 1 request = 1 proxy
        session_id = request.meta.get('luminati_session_id',random.random())

        # Random user agent
        j = int(session_id * len(self.user_agents))
        request.headers['user-agent'] = self.user_agents[j]

        # Set proxy
        _proxy = self.url % (self._username, session_id, self._password, self.port)
        request.meta['proxy'] = _proxy

        # Reset Proxy-Authorization
        try:
            del request.headers['Proxy-Authorization']
        except:
            pass

        # DEBUG ONLY - USE CAREFULLY - PLEASE NOT TOO MANY REQUESTS!!!
        if self.debug:
            proxy = urllib.request.ProxyHandler({'http': _proxy})
            opener = urllib.request.build_opener(proxy)
            res = opener.open('http://lumtest.com/myip.json').read()
            res = ast.literal_eval(res) if res else {}
            logger.info("[LUMINATI_ROTATE_IP_MIDDLEWARE][PROCESS_REQUEST][NEUKOLLN] Using IP ==========> %s, "
                        "Country ==========> %s, Proxy  ==========> %s" % (res.get('ip', 'Unknown'),
                                                                           res.get('country', 'Unknown'),
                                                                           _proxy))

    def process_response(self, request, response, spider):
        """Interesting to check cached page"""

        # Check if Ip has been banned
        is_ban = getattr(spider, 'response_is_ban')
        ban = is_ban(request, response)

        # If Ip has been banned
        if ban:

            # Get url or redirected url
            url = request.meta.get('redirect_urls', [request.url])[0] if request.meta else request.url

            # [INFO] Alert user
            logger.info(
                "[LUMINATI_ROTATE_IP_MIDDLEWARE][PROCESS_RESPONSE][NEUKOLLN] Response has been detected as banned; "
                "response.url: %s; retry this url: %s;" % (response.url, url))

            # Retrieve session_id if exists else random e.g. reset session each time: 1 request = 1 proxy
            session_id = request.meta.get('luminati_session_id', random.random())

            # Random user agent
            j = int(session_id * len(self.user_agents))
            request.headers['user-agent'] = self.user_agents[j]

            # Set proxy
            _proxy = self.url % (self._username, session_id, self._password, self.port)
            request.meta['proxy'] = _proxy

            # Reset Proxy-Authorization
            try:
                del request.headers['Proxy-Authorization']
            except:
                pass

            request.meta[NEUKOLLN_META_BANNED_KEY] = ban
            request.meta[NEUKOLLN_META_REFRESH_CACHE_KEY] = True # refresh cache!!!
            request.dont_filter = True  # DON'T FILTER!!!
            request = request.replace(url=url)

            return request

        # Return response and process it
        return response

class NeukollnBaseSpider(object):
    def response_is_ban(self, request, response):
        """You can override or complete this method in your own spider if needed..."""
        ban = False

        # Check if there is a body
        bool = ((response.status == 200) and not len(response.body))
        if bool:
            logger.error("[RESPONSE_IS_BAN][NEUKOLLN_BASE_SPIDER][NEUKOLLN] response.status == 200 but body is empty")
        ban = ban or bool

        # Check the url
        bool = ("erreur" in response.url) or ("error" in response.url)
        if bool:
            logger.error("[RESPONSE_IS_BAN][NEUKOLLN_BASE_SPIDER][NEUKOLLN] \"error\" in url")
        ban = ban or bool

        # Check inside the body if "captcha" keyword
        try:
            bool = b'captcha' in response.body.lower() or b'distilnetworks' in response.body.lower()
        except UnicodeDecodeError:
            bool = 'captcha' in response.body.decode('latin-1').encode("utf-8").lower() or 'distilnetworks' in response.body.decode('latin-1').encode("utf-8").lower()
        if bool:
            logger.error("[RESPONSE_IS_BAN][NEUKOLLN_BASE_SPIDER][NEUKOLLN] \"captcha\" in url")
        ban = ban or bool

        # Inform user
        requested_url = request.meta.get('redirect_urls', [request.url])[0] if request.meta else request.url
        logger.debug("[RESPONSE_IS_BAN][NEUKOLLN_BASE_SPIDER][NEUKOLLN] "
                     "%s, response.status=%s, response.url=%s, requested url=%s"
                     % (str(ban), str(response.status), response.url, requested_url))

        # Return boolean
        return ban




##---------aide
# dans settings

# 'dossier.gabesmid.LuminatiRotateIpAddressMiddleware': 1,

# dans spider
# #---
# from dossier.gabesmid import  NeukollnBaseSpider
# #---


# class nom_class(NeukollnBaseSpider,scrapy.Spider):

# #---


#     luminati_username = "lum-customer-autobiz-zone-pige_auto_generic_world"
#     luminati_password = "rs8y0xdvz2wh"
#     luminati_allow_debug = False
# #---
#     def __init__(self, *args, **kwargs):
#         super(Nom_spider, self).__init__(*args, **kwargs)
#                         # ...


#     def response_is_ban(self, request, response):
#                     # use default rules, but also consider HTTP 200 responses
#                             # a ban if there is 'captcha' word in response body.
#         ban = super(Nom_spider, self).response_is_ban(request, response)
#                                             # ban = ban or 'captcha' in response.body.lower()
#         return ban

# #---

#-------------new storm proxy

class NewStormproxiesMiddleware(NeukollnBaseMiddleware):
    """Middleware tu use the service"""
    _main_gateway = [
            "5.79.73.131:13400","5.79.66.2:13401",
    ]

    _3_minutes = [
        "69.30.240.226:15014",
        "69.30.197.122:15014",
        "142.54.177.226:15014",
        "198.204.228.234:15014",
        "69.30.240.226:15015",
        "69.30.197.122:15015",
        "142.54.177.226:15015",
        "198.204.228.234:15015",
        "69.30.240.226:15016",
        "69.30.197.122:15016",
        "142.54.177.226:15016",
        "198.204.228.234:15016",
        "69.30.240.226:15017",
        "69.30.197.122:15017",
        "142.54.177.226:15017",
        "198.204.228.234:15017",
        "69.30.240.226:15018",
        "69.30.197.122:15018",
        "142.54.177.226:15018",
        "198.204.228.234:15018",
        "69.30.240.226:15019",
        "69.30.197.122:15019",
        "142.54.177.226:15019",
        "198.204.228.234:15019",
        "69.30.240.226:15020",
        "69.30.197.122:15020",
        "142.54.177.226:15020",
        "198.204.228.234:15020",
        "69.30.240.226:15021",
        "69.30.197.122:15021",
        "142.54.177.226:15021",
        "198.204.228.234:15021",
        "69.30.240.226:15022",
        "69.30.197.122:15022",
        "142.54.177.226:15022",
        "198.204.228.234:15022",
        "69.30.240.226:15023",
        "69.30.197.122:15023",
        "142.54.177.226:15023",
        "198.204.228.234:15023",
        "195.154.255.118:15014",
        "195.154.222.228:15014",
        "195.154.252.58:15014",
        "195.154.222.26:15014",
        "195.154.255.118:15015",
        "195.154.222.228:15015",
        "195.154.252.58:15015",
        "195.154.222.26:15015",
        "195.154.255.118:15016",
        "195.154.222.228:15016",
        "195.154.252.58:15016",
        "195.154.222.26:15016",
        "195.154.255.118:15017",
        "195.154.222.228:15017",
        "195.154.252.58:15017",
        "195.154.222.26:15017",
        "195.154.255.118:15018",
        "195.154.222.228:15018",
        "195.154.252.58:15018",
        "195.154.222.26:15018",
        "195.154.255.118:15019",
        "195.154.222.228:15019",
        "195.154.252.58:15019",
        "195.154.222.26:15019",
        "195.154.255.118:15020",
        "195.154.222.228:15020",
        "195.154.252.58:15020",
        "195.154.222.26:15020",
        "195.154.255.118:15021",
        "195.154.222.228:15021",
        "195.154.252.58:15021",
        "195.154.222.26:15021",
        "195.154.255.118:15022",
        "195.154.222.228:15022",
        "195.154.252.58:15022",
        "195.154.222.26:15022",
        "195.154.255.118:15023",
        "195.154.222.228:15023",
        "195.154.252.58:15023",
        "195.154.222.26:15023",




    ]

    _15_minutes = [
        "63.141.241.98:16001",
        "173.208.209.42:16001",
        "69.197.179.122:16001",
        "173.208.199.74:16001",
        "163.172.36.211:16001",
        "163.172.36.213:16001",
        "163.172.214.109:16001",
        "163.172.214.117:16001",
    ]

    _proxies_duration = [
        # duration in seconds
        (_main_gateway, 0),
        (_3_minutes, 3 * 60),
        (_15_minutes, 15 * 60)
    ]

    stormproxies_proxies_duration_dict = {}  # build in __init__ function
    stormproxies_proxies_last_used_dict = {}  # build in __init__ function

    def __init__(self):
        # Build stormproxies_proxies_duration_dict, stormproxies_proxies_last_used_dict
        yesterday = datetime.now() - timedelta(days=1)
        for proxies, duration in self._proxies_duration:
            for proxy in proxies:
                self.stormproxies_proxies_duration_dict[proxy] = duration
                self.stormproxies_proxies_last_used_dict[proxy] = yesterday  # initialization with yesterday

        logger.debug("[STORMPROXIES_MIDDLEWARE][__INIT__][NEUKOLLN] stormproxies_proxies_duration_dict=%s" % str(self.stormproxies_proxies_duration_dict))
        logger.debug("[STORMPROXIES_MIDDLEWARE][__INIT__][NEUKOLLN] stormproxies_proxies_last_used_dict=%s" % str(self.stormproxies_proxies_last_used_dict))

        # Set list of user agent
        self.user_agents = get_project_settings().get(NEUKOLLN_SETTINGS_USER_AGENT_CHOICES)
        if not self.user_agents:
            # [DEBUG] Alert user
            logger.debug("[STORMPROXIES_MIDDLEWARE][__INIT__][NEUKOLLN] %s is not set in the settings so a default "
                         "list of user agents from the library will be used." % NEUKOLLN_SETTINGS_USER_AGENT_CHOICES)
            self.user_agents = NEUKOLLN_USER_AGENT_DEFAULT_LIST

    def spider_opened(self, spider):
        pass

    def get_user_agent_for_proxy(self, proxy):
        i = list(self.stormproxies_proxies_duration_dict.keys()).index(proxy)
        j = i % len(self.user_agents)
        return self.user_agents[j]

    def get_available_proxies(self):
        _now = datetime.now()
        res = []
        for proxy, last_used in self.stormproxies_proxies_last_used_dict.items():
            if not self.stormproxies_proxies_duration_dict[proxy] or abs((last_used - _now).seconds) > self.stormproxies_proxies_duration_dict[proxy]:
                logger.debug("%s %s %s %d %d" % (proxy, last_used, _now, (_now - last_used).seconds, self.stormproxies_proxies_duration_dict[proxy]))
                res.append(proxy)
        return res

    def set_proxy(self, request):
        """
        Set proxy for given request
        :param request:
        :return:
        """
        # Reset Proxy-Authorization
        try:
            del request.headers['Proxy-Authorization']
        except:
            pass

        # Get available proxies
        available_proxies = self.get_available_proxies()

        # Random index and proxy among available proxies
        i = int(random.random() * len(available_proxies))
        proxy = available_proxies[i]
        request.meta['proxy'] = proxy

        # Update its last used value
        self.stormproxies_proxies_last_used_dict[proxy] = datetime.now()

        # Alert user
        logger.debug("[STORMPROXIES_MIDDLEWARE][__INIT__][NEUKOLLN] "
                     "Using proxy %s, %d proxies available" % (proxy, len(available_proxies)))

        # Set user-agent
        request.headers['user-agent'] = self.get_user_agent_for_proxy(proxy)

        return request

    def process_request(self, request, spider):
        """Set the correct IP using the pool of Ips"""
        self.set_proxy(request)

    def process_response(self, request, response, spider):
        """Interesting to check cached page"""

        # Check if Ip has been banned
        is_ban = getattr(spider, 'response_is_ban')
        ban = is_ban(request, response)

        # If Ip has been banned
        if ban:
            # Get url or redirected url
            url = request.meta.get('redirect_urls', [request.url])[0] if request.meta else request.url

            self.set_proxy(request)
            request.meta[NEUKOLLN_META_BANNED_KEY] = ban
            request.meta[NEUKOLLN_META_REFRESH_CACHE_KEY] = True  # refresh cache!!!
            request.dont_filter = True  # DON'T FILTER!!!
            request = request.replace(url=url)

            # [INFO] Alert user
            logger.info("[STORMPROXIES_MIDDLEWARE][PROCESS_RESPONSE][NEUKOLLN] Response has been detected as banned; response.url: %s; retry this url: %s; request: %s" % (response.url, url, str(request)))
            return request

        # Return response and process it
        return response

#----------------------ancien storm proxy


class StormproxiesMiddleware(NeukollnBaseMiddleware):
    """Middleware tu use the service"""
    _main_gateway = [
        "108.59.14.200:13402",
    ]

    _3_minutes = [
            "163.172.48.109:15014",
            "163.172.48.117:15014",
            "163.172.48.119:15014",
            "163.172.48.121:15014",
            "163.172.48.109:15015",
            "163.172.48.117:15015",
            "163.172.48.119:15015",
            "163.172.48.121:15015",
            "163.172.48.109:15016",
            "163.172.48.117:15016",
            "163.172.48.119:15016",
            "163.172.48.121:15016",
            "163.172.48.109:15017",
            "163.172.48.117:15017",
            "163.172.48.119:15017",
            "163.172.48.121:15017",
            "163.172.48.109:15018",
            "163.172.48.117:15018",
            "163.172.48.119:15018",
            "163.172.48.121:15018",
            "163.172.48.109:15019",
            "163.172.48.117:15019",
            "163.172.48.119:15019",
            "163.172.48.121:15019",
            "163.172.48.109:15020",
            "163.172.48.117:15020",
            "163.172.48.119:15020",
            "163.172.48.121:15020",
            "163.172.48.109:15021",
            "163.172.48.117:15021",
            "163.172.48.119:15021",
            "163.172.48.121:15021",
            "163.172.48.109:15022",
            "163.172.48.117:15022",
            "163.172.48.119:15022",
            "163.172.48.121:15022",
            "163.172.48.109:15023",
            "163.172.48.117:15023",
            "163.172.48.119:15023",
            "163.172.48.121:15023",
            "163.172.36.181:15014",
            "163.172.36.191:15014",
            "163.172.36.197:15014",
            "163.172.36.207:15014",
            "163.172.36.181:15015",
            "163.172.36.191:15015",
            "163.172.36.197:15015",
            "163.172.36.207:15015",
            "163.172.36.181:15016",
            "163.172.36.191:15016",
            "163.172.36.197:15016",
            "163.172.36.207:15016",
            "163.172.36.181:15017",
            "163.172.36.191:15017",
            "163.172.36.197:15017",
            "163.172.36.207:15017",
            "163.172.36.181:15018",
            "163.172.36.191:15018",
            "163.172.36.197:15018",
            "163.172.36.207:15018",
            "163.172.36.181:15019",
            "163.172.36.191:15019",
            "163.172.36.197:15019",
            "163.172.36.207:15019",
            "163.172.36.181:15020",
            "163.172.36.191:15020",
            "163.172.36.197:15020",
            "163.172.36.207:15020",
            "163.172.36.181:15021",
            "163.172.36.191:15021",
            "163.172.36.197:15021",
            "163.172.36.207:15021",
            "163.172.36.181:15022",
            "163.172.36.191:15022",
            "163.172.36.197:15022",
            "163.172.36.207:15022",
            "163.172.36.181:15023",
            "163.172.36.191:15023",
            "163.172.36.197:15023",
            "163.172.36.207:15023",





    ]

    _15_minutes = [
        "63.141.241.98:16001",
        "199.168.137.38:16001",
        "69.197.179.122:16001",
        "104.193.9.19:16001",
        "163.172.36.211:16001",
        "163.172.36.213:16001",
        "163.172.214.109:16001",
        "163.172.214.117:16001",
    ]

    _proxies_duration = [
        # duration in seconds
        (_main_gateway, 0),
        (_3_minutes, 3 * 60),
        (_15_minutes, 15 * 60)
    ]

    stormproxies_proxies_duration_dict = {}  # build in __init__ function
    stormproxies_proxies_last_used_dict = {}  # build in __init__ function

    def __init__(self):
        # Build stormproxies_proxies_duration_dict, stormproxies_proxies_last_used_dict
        yesterday = datetime.now() - timedelta(days=1)
        for proxies, duration in self._proxies_duration:
            for proxy in proxies:
                self.stormproxies_proxies_duration_dict[proxy] = duration
                self.stormproxies_proxies_last_used_dict[proxy] = yesterday  # initialization with yesterday

        logger.debug("[STORMPROXIES_MIDDLEWARE][__INIT__][NEUKOLLN] stormproxies_proxies_duration_dict=%s" % str(self.stormproxies_proxies_duration_dict))
        logger.debug("[STORMPROXIES_MIDDLEWARE][__INIT__][NEUKOLLN] stormproxies_proxies_last_used_dict=%s" % str(self.stormproxies_proxies_last_used_dict))

        # Set list of user agent
        self.user_agents = get_project_settings().get(NEUKOLLN_SETTINGS_USER_AGENT_CHOICES)
        if not self.user_agents:
            # [DEBUG] Alert user
            logger.debug("[STORMPROXIES_MIDDLEWARE][__INIT__][NEUKOLLN] %s is not set in the settings so a default "
                         "list of user agents from the library will be used." % NEUKOLLN_SETTINGS_USER_AGENT_CHOICES)
            self.user_agents = NEUKOLLN_USER_AGENT_DEFAULT_LIST

    def spider_opened(self, spider):
        pass

    def get_user_agent_for_proxy(self, proxy):
        i = list(self.stormproxies_proxies_duration_dict.keys()).index(proxy)
        j = i % len(self.user_agents)
        return self.user_agents[j]

    def get_available_proxies(self):
        _now = datetime.now()
        res = []
        for proxy, last_used in self.stormproxies_proxies_last_used_dict.items():
            if not self.stormproxies_proxies_duration_dict[proxy] or abs((last_used - _now).seconds) > self.stormproxies_proxies_duration_dict[proxy]:
                logger.debug("%s %s %s %d %d" % (proxy, last_used, _now, (_now - last_used).seconds, self.stormproxies_proxies_duration_dict[proxy]))
                res.append(proxy)
        return res

    def set_proxy(self, request):
        """
        Set proxy for given request
        :param request:
        :return:
        """
        # Reset Proxy-Authorization
        try:
            del request.headers['Proxy-Authorization']
        except:
            pass

        # Get available proxies
        available_proxies = self.get_available_proxies()

        # Random index and proxy among available proxies
        i = int(random.random() * len(available_proxies))
        proxy = available_proxies[i]
        request.meta['proxy'] = proxy

        # Update its last used value
        self.stormproxies_proxies_last_used_dict[proxy] = datetime.now()

        # Alert user
        logger.debug("[STORMPROXIES_MIDDLEWARE][__INIT__][NEUKOLLN] "
                     "Using proxy %s, %d proxies available" % (proxy, len(available_proxies)))

        # Set user-agent
        request.headers['user-agent'] = self.get_user_agent_for_proxy(proxy)

        return request

    def process_request(self, request, spider):
        """Set the correct IP using the pool of Ips"""
        self.set_proxy(request)

    def process_response(self, request, response, spider):
        """Interesting to check cached page"""

        # Check if Ip has been banned
        is_ban = getattr(spider, 'response_is_ban')
        ban = is_ban(request, response)

        # If Ip has been banned
        if ban:
            # Get url or redirected url
            url = request.meta.get('redirect_urls', [request.url])[0] if request.meta else request.url

            self.set_proxy(request)
            request.meta[NEUKOLLN_META_BANNED_KEY] = ban
            request.meta[NEUKOLLN_META_REFRESH_CACHE_KEY] = True  # refresh cache!!!
            request.dont_filter = True  # DON'T FILTER!!!
            request = request.replace(url=url)

            # [INFO] Alert user
            logger.info("[STORMPROXIES_MIDDLEWARE][PROCESS_RESPONSE][NEUKOLLN] Response has been detected as banned; response.url: %s; retry this url: %s; request: %s" % (response.url, url, str(request)))
            return request

        # Return response and process it
        return response
