# -*- coding: utf-8 -*-

# Scrapy settings for newPropiedades project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'newPropiedades'

SPIDER_MODULES = ['newPropiedades.spiders']
NEWSPIDER_MODULE = 'newPropiedades.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newPropiedades (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 4

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'newPropiedades.middlewares.NewpropiedadesSpiderMiddleware': 1,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
RETRY_TIMES= 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 416,405,403,429,302,301,508,400]
DOWNLOADER_MIDDLEWARES = {
#    'newPropiedades.middlewares.NewpropiedadesSpiderMiddleware': 1,

    'newPropiedades.gabesmid.LuminatiRotateIpAddressMiddleware': 1,

#    'newPropiedades.gabesmid.StormproxiesMiddleware': 1,

#      'newPropiedades.gabesmid.NewStormproxiesMiddleware': 1,

#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,

 #   'scrapy_proxies.RandomProxy': 100,
 #   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,

    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 901,


#'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700 #newwwwwwwwwww
}

#PROXY_LIST="/home/h.guiza/admin/mission/newPropiedades/octobre2018/proxy.txt"

#PROXY_MODE= 0

#CUSTOM_PROXY ='http://108.59.14.200:13402' 

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'newPropiedades.pipelines.NewpropiedadesPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings

#HTTPCACHE_IGNORE_MISSING=True

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = '/home/m.hamouda/cacheWare/propiedades/'
HTTPCACHE_IGNORE_HTTP_CODES = [500, 502, 503, 504, 408, 416,405,403,429,302,301,508,404,400]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#FEED_EXPORT_ENCODING = 'windows-1250'

import time, os
path = "/home/m.hamouda/newPropiedades/newPropiedades/spiders/logs"
if not os.path.exists(path):
            os.makedirs(path)
now = time.strftime("%Y%m%d_%Hh-%Mmin-%Ss")
LOG_FILE = "%s/%s_%s.log" % (path, 'newPropiedades', now)
###
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = True

