# -*- coding:utf-8 -*-
'''
@time   : 2018-08-13 15:22
@author : Zephyr
@file   : 06爬取网易云.py
'''

import urllib
from urllib import request, parse
import json

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh,en;q=0.9,zh-CN;q=0.8",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "_ntes_nuid=26ba6011fc01e9a6a67ccd1a88c0bff5; vjuids=ab4a25d16.15e2ddd0814.0.1f380095ceed6; _ngd_tid=CwSwbl4OPH24VPVbh89FMr0EBQuCnx6N; nts_mail_user=fate162@163.com:-1:1; P_INFO=fate162@163.com|1519811822|0|other|00&99|gud&1515738914&mail163#gud&440300#10#0#0|&0||fate162@163.com; _ga=GA1.2.1712908077.1501678337; _iuqxldmzr_=32; WM_TID=jF2my7uo%2Fg6l8%2Ff60RRPIos87nC1BBlJ; vjlast=1504008014.1533103158.22; vinfo_n_f_l_n3=5d3156d7cd58b491.1.5.1504163435567.1521508584755.1533103171109; __f_=1533279750309; _ntes_nnid=26ba6011fc01e9a6a67ccd1a88c0bff5,1533729035356; JSESSIONID-WYYY=uGU46gZ6DFr%2BTBRhI4FmV7eky1CocNH77wAIjDX3fW%2F8Zy4dlGs0Y1E4v5ldbNSt7pWF8s76kgkd3ful9sXucu6wbX%2ByDCUXJHc84h3AOhFx6Xxblo1u4I52boXVxRiGNrr%2BWceTnRI5%2B3UAvYqI0Ap2aP2sw6%5CkT%2FbypcHR6pMHj%5Cau%3A1534146718412; __utma=94650624.1712908077.1501678337.1533729036.1534144919.18; __utmc=94650624; __utmz=94650624.1534144919.18.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=VRMXvWI7BWQB%2BGBKy8cMSJtmtIpqHjizlnIJRxDOgv59GO4Xy0OtUZ3WE7H%2FtpIzjGqqFmUomiHQxO3VAVjLNUe6m8aAFn%2BJ2YiU6wr%2BJ2fdUSggDv%2BZQ0f9pXxfnEScbmM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89aa25fc94a9a5d362aef0fda6f24af6879bd6c933f6a9f8d8d868838fa9a9b82af0fea7c3b92a968e83b9f55d8be98eb8d44ae9998eacfc34a1939dabf767b897c092cb62aba6a48fcc4292a88cb0e67ef7e789b0b754bbf08195d852f1898bd8cb25b8b0879be94db3af8a8ed865afb788b2fb45f18a8fb7e9488e8babd7f034a39f8a8faa42f287a7b6b57db2f586d3e570978da988c77ee9869fd1e533b488b887ed4f91bdae8ed037e2a3; __utmb=94650624.10.10.1534144919; playerid=72077042",
    "Host": "music.163.com",
    "Origin": "https://music.163.com",
    "Referer": "https://music.163.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='

data = {
    "params": "qqRcyn6y4WlsY0+IyKdxrHZvD29CmQ31xXkjtyyoK+04OHanX2b1MtYimGC5RR5CZ+c93Q74d5K3WaIbDcwuW4i9bOyNoKKGMdd/x4l60RrebzYGHjwaO0nm/FMhFjDz",
    "encSecKey": "6cd1c70ae0d7a67f3be74c6f934484fec1cc896dfa0ca4af3e21969d7c1e914993b2741f2a4445ec0b97f2aa1012c61dfad536f8d45c9dd56d13b680ddd8c99b406283e5d0b78e508d6a56315238ed62c3fa6a962bca97988379d42639f8070906c625b4ef799c14f35a0e3dbde226cbc8d206fe1618d123d84549bea3d6233a",
}

data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req).read().decode('gb2312', 'ignore')
# print(response)


musicUrl = json.loads(response)['data'][0]['url']
print(musicUrl)

with open('一个人.mp3', 'wb') as f:
    res = urllib.request.urlopen(musicUrl).read()
    f.write(res)

    # https://music.163.com/song/media/outer/url?id=28987167.mp3
