# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 09:13
@author : Zephyr
@file   : 01handler.py
'''

import urllib
from urllib import request

# 处理器  处理HTTPS
handler = urllib.request.HTTPSHandler()
# handler = urllib.request.HTTPHandler()

# 打开器
opener = urllib.request.build_opener(handler)

url = 'http://www.baidu.com/'
res_ = urllib.request.urlopen(url)
print(res_)
'''
fullurl, data=None, timeout=socket
'''

# 通过打开器 打开网页
response = opener.open(url)

# print(response.read().decode())

# 安装 opener,  全局的opener
urllib.request.install_opener(opener)

res = urllib.request.urlopen(url)
print(res)
