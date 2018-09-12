# -*- coding:utf-8 -*-
'''
@time   : 2018-08-13 16:42
@author : Zephyr
@file   : 01urllib.py
'''
import urllib.request  # urllib2

# 伪装
import sys

'''
Accept: text/html,image/webp,image/apng,*/*;q=0.8 可接收类型
Accept-Encoding: gzip, deflate, br  可接收压缩类型，做爬虫不发送这条
Accept-Language: zh,en;q=0.9,zh-CN;q=0.8 语言
Cache-Control: max-age=0
Connection: keep-alive  连接
Cookie: BIDUPSID=BCD315DCE8F7FF6947455A0DE12663EB;
Upgrade-Insecure-Requests: 1
Referer: https://www.baidu.com/ 来自哪里
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
'''

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh,en;q=0.9,zh-CN;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "BIDUPSID=BCD315DCE8F7FF6947455A0DE12663EB; PSTM=1501484586; MCITY=-%3A; BAIDUID=2F5F2F9E96D78C3CB5613B1F94327B12:FG=1; BD_UPN=12314753; delPer=0; ispeed_lsm=26; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; BD_HOME=0; BDRCVFR[Elku9xRgn_n]=azWxGYybh8Rfjb3njDznj63g1NxuAT; H_PS_PSSID=",
    "Host": "www.baidu.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

# 构造一个请求体
'''
url, data=None,
headers={},
'''

req = urllib.request.Request('https://www.baidu.com/', headers=headers)
# 打开请求体
response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))

print(response.info())

__version__ = '%d.%d' % sys.version_info[:2]

print('Python-urllib/%s' % __version__)
