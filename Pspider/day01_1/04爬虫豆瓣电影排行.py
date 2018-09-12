# -*- coding:utf-8 -*-
'''
@time   : 2018-08-13 14:03
@author : Zephyr
@file   : 04爬虫豆瓣电影排行.py
'''
import urllib
from urllib import request
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

i = 0
while True:
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d" % (i * 20)
    i += 1

    # 增量爬虫（续爬，更新）
    # 连接redis -- 待爬取队列，以爬取队列
    # 将url传入redis md5 编码
    # 第二进来，先查看redis是否有该条url
    # 没有就爬

    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    if response.code == 200:
        moviedata = response.read().decode('utf-8')
        # 电影数据
        data = json.loads(moviedata)['data']
        for movie in data:
            directors = movie['directors']
            rate = movie['rate']
            print(directors, rate)
    else:
        print(i)
        break
