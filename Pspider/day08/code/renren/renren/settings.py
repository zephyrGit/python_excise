# -*- coding: utf-8 -*-

# Scrapy settings for renren project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'renren'

SPIDER_MODULES = ['renren.spiders']
NEWSPIDER_MODULE = 'renren.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'renren (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'renren.middlewares.RenrenSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'renren.middlewares.RandomCookieMiddleware': 543,
    'renren.middlewares.SeleniumMiddleware': 540,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'renren.pipelines.RenrenPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


PROXIES = ['39.135.35.18:80', '39.135.35.19:80', '39.135.35.16:80', '94.74.191.83:80', '120.24.152.123:3128',
           '39.135.35.17:80', '103.242.219.242:8080', '116.197.131.212:8080', '103.232.33.6:21231',
           '46.29.12.231:53281', '171.4.217.191:8080', '124.193.37.5:8888', '185.48.142.27:41258',
           '103.85.112.51:53281', '112.126.65.236:80', '120.78.180.231:8118', '194.146.230.9:41258',
           '50.201.51.216:8080', '101.236.41.207:3128', '116.58.38.242:80', '187.190.221.71:3128',
           '103.85.234.210:53281', '223.202.204.195:80', '203.130.46.108:9090', '103.218.26.98:8080',
           '77.247.93.212:53281', '188.235.146.116:53281', '175.184.248.231:53281', '140.143.105.243:80',
           '47.75.103.235:3128', '83.147.220.57:53281', '41.169.154.2:9001', '91.238.23.83:41258', '213.21.23.98:53281',
           '203.78.141.118:8080', '181.112.153.14:53281', '170.84.145.131:8080', '124.105.29.184:3128',
           '182.23.110.70:8080', '187.87.180.132:20183', '49.51.68.122:1080', '190.90.140.82:53281',
           '190.96.73.170:3128', '49.51.70.42:1080', '46.30.220.177:41258', '49.51.195.24:1080', '46.98.43.103:53281',
           '101.231.188.78:8080', '49.51.228.166:1080', '213.148.166.161:53281', '125.39.9.35:9000',
           '60.30.19.131:10010', '125.39.9.34:9000', '124.238.248.4:80', '60.8.42.137:8908', '218.201.55.74:63000',
           '222.222.236.207:8060', '222.223.203.109:8060', '124.42.68.152:90', '121.17.18.219:8060', '218.60.8.98:3129',
           '218.60.8.99:3129', '218.60.8.83:3129', '222.33.192.238:8118', '218.106.205.145:8080', '120.131.9.254:1080',
           '59.44.247.194:9797', '60.14.125.246:8908', '116.62.194.248:3128', '218.106.98.166:53281',
           '121.40.138.161:8000', '121.43.235.100:90', '183.129.207.73:18186', '58.87.68.189:1080', '58.87.98.112:1080',
           '111.3.108.44:8118', '183.129.207.77:10000', '122.224.34.152:808', '202.107.195.217:80',
           '223.93.172.248:3128', '183.129.207.73:15823', '36.33.25.100:808', '222.195.66.216:1080', '36.33.25.228:808',
           '218.207.212.86:80', '125.77.25.123:80', '119.27.177.169:80', '117.127.0.203:8080', '117.127.0.201:8080',
           '117.127.0.195:8080', '117.127.0.196:8080', '117.127.0.198:8080', '117.127.0.198:80', '117.127.0.196:80',
           '117.127.0.195:80', '182.106.140.118:80', '182.106.140.122:80', '182.106.140.120:80', '117.44.247.37:8908',
           '117.127.0.197:8080', '117.127.0.203:80', '117.127.0.205:8080', '117.127.0.205:80', '117.127.0.201:80',
           '117.127.0.197:80', '221.2.174.28:8060', '223.96.95.229:3128', '222.175.200.58:8060', '221.2.175.238:8060',
           '221.2.155.35:8060', '221.2.174.6:8060', '115.28.4.185:8118', '221.1.205.74:8060', '221.2.174.99:8060',
           '113.128.198.50:8060', '221.2.174.3:8060', '171.10.31.67:8080', '115.159.143.108:80', '36.99.17.52:80',
           '115.159.31.195:8080', '222.88.154.56:8060', '120.194.61.62:8060', '125.46.0.62:53281', '123.7.61.8:53281',
           '222.89.85.158:8060', '221.14.140.130:80', '42.236.123.17:80', '221.14.140.66:80', '36.99.206.240:61234',
           '219.150.189.212:9999', '58.49.72.141:8888', '58.49.73.141:8888', '222.242.171.5:63000', '175.9.79.65:8060',
           '103.38.197.42:53281', '183.62.22.220:3128', '119.28.118.116:1080', '27.46.75.5:9000', '120.198.67.93:63000',
           '183.62.196.10:3128', '14.116.179.185:3128', '121.8.98.198:80', '36.36.115.170:8197', '120.236.178.117:8118',
           '119.28.194.66:8888', '119.28.142.148:8888', '58.250.23.210:1080', '202.46.42.156:8080', '27.46.74.5:9999',
           '202.46.42.156:80', '119.5.0.41:1133', '106.56.102.129:8070', '123.249.88.153:9000', '113.200.56.13:8010',
           '106.56.102.88:8070', '106.56.102.239:8070', '61.150.113.27:8908', '117.35.51.66:53281',
           '113.200.81.90:41766', '61.178.49.31:8908', '111.44.243.254:8123', '202.100.83.139:80', '117.156.234.3:8060',
           '113.196.135.99:3128', '211.75.82.206:3128', '61.63.0.109:3128', '1.172.185.143:53281',
           '125.72.232.180:8070', '118.171.184.215:3128', '1.34.1.60:21776', '60.250.79.187:80', '122.116.253.158:8082',
           '175.181.40.61:8080', '221.7.255.167:80', '118.24.61.165:8118', '118.24.85.28:3128', '110.72.242.203:53281',
           '118.24.121.231:3128', '118.24.88.66:1080', '118.24.172.37:1080', '118.24.151.117:8088', '221.7.255.168:80',
           '221.7.255.167:8080', '60.13.156.45:8060', '124.118.27.3:8060', '121.46.95.65:8080', '103.251.36.41:80',
           '61.93.84.86:3128', '39.106.160.36:3128', '119.28.52.15:1080', '119.28.32.250:1080', '113.253.113.90:8380',
           '39.108.193.131:80', '27.98.206.186:3128', '119.28.51.117:80', '61.239.43.47:3128', '220.246.169.40:8080',
           '39.104.122.119:8888', '202.175.105.226:8080', '202.175.105.228:8080', '202.175.124.11:8080',
           '101.4.136.34:80', '61.145.182.27:53281', '219.141.153.41:80', '112.193.129.125:8118', '182.18.57.27:808',
           '118.25.18.67:80', '123.169.39.236:808', '175.155.141.50:1133', '190.151.10.226:8080', '46.101.215.222:8118',
           '81.18.214.62:8080', '85.185.238.214:8080', '115.211.7.93:808', '106.56.102.157:8070', '59.39.128.95:9000',
           '114.250.25.19:80', '171.107.140.152:53281', '163.125.252.107:9797', '113.76.96.66:9797',
           '118.89.38.21:8080', '113.104.236.188:9000', '140.143.96.216:80', '118.31.0.140:3128', '112.91.218.21:9000',
           '111.230.35.85:1080', '221.7.255.168:8080']

COOKIE = [
    {'RK': 'rmHT7e2LQD', 'pgv_pvi': '9920637952', 'pac_uid': '1_1687458949',
     'eas_sid': 'H1z5Y0H4U3M3f8E004v1F3X6I7', 'LW_uid': 'Y1W590G4O333K87114z6Z4L5J4',
     'pgv_pvid_new': '1687458949_103e8ac4183', 'tvfe_boss_uuid': '5eed6635b6c9405a',
     'mobileUV': '1_15ecd77b5fe_99bfa', 'o_cookie': '1687458949', 'QZ_FE_WEBP_SUPPORT': '1',
     'pgv_pvid': '2040220332', 'ptcz': '1fd2762d2f45e34542eb5fcd75ac829861fc1c6ac443d23fccfd1ce0edd2fc9a',
     '__Q_w_s__QZN_TodoMsgCnt': '1', 'ptui_loginuin': '1687458949', 'pt2gguin': 'o1687458949',
     'LW_sid': 'B1b5G3E3O931C7e8h9X6l7Z0q4', 'luin': 'o1687458949',
     'lskey': '0001000089894b46be89448efe29901858b8f0dc97ddb536699ad2bb0b528d8c0980b2fbd3228a5894bcd854',
     '_qpsvr_localtk': '0.9360270193842759', 'pgv_si': 's4745961472', 'ptisp': 'ctc',
     'pgv_info': 'ssid=s2811748556', 'uin': 'o1687458949', 'skey': '@s6Fnk2wO4', 'p_uin': 'o1687458949',
     'Loading': 'Yes', 'qz_screen': '1366x768', '1687458949_todaycount': '0', '1687458949_totalcount': '0',
     'cpu_performance_v8': '59', 'pt4_token': 'HHnu8SWWN-cYqkZPJkAbqpsPaJ1Qj*3HPVpB5FzJ19U_',
     'p_skey': 'io2JKmEvT9mttLS2ayZAoZAax9N2zSPonIB*m8fPt64_',
     'x-stgw-ssl-info': 'c2a39c2c272775873d1cb51c2782c877|0.102|1534987292.958|36|.|I|TLSv1.2|ECDHE-RSA-AES128-GCM-SHA256|22000|h2|0'}
]
