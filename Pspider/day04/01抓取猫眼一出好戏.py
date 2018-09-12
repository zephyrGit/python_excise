# -*- coding:utf-8 -*-
'''
@time   : 2018-08-16 08:48
@author : Zephyr
@file   : 01抓取猫眼一出好戏.py
'''
import lxml
from lxml import etree
import requests
import json
import math

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}


def getMovieJson(url):
    '''
    获取电影评论信息
    :param url:
    :return:
    '''

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html = response.text
        return html
    else:
        return None


def parse_one_page(html):
    '''
    解析每一页数据
    :param html:网页源码
    :return:
    '''
    if html:
        data = json.loads(html)['cmts']
        for item in data:
            yield {
                'nickName': item['nickName'],
                'cityName': item['cityName'],
                'content': item['content'].strip().replace('\n', ''),
                'score': item['score'],
                'startTime': item['startTime']
            }


def save_to_txt(url):
    '''
    保存到文件
    :param url:
    :return:
    '''

    html = getMovieJson(url)

    with open('一出好戏.txt', 'a+', encoding='utf-8', errors='ignore') as f:
        for item in parse_one_page(html):
            print(item)
            f.write(str(item['startTime'] + "," + item['nickName']
                        + "," + item['cityName'] + "," + str(item['score'])
                        + "," + item['content'] + '\n'))


if __name__ == '__main__':
    pageNum = math.ceil(73633 / 15)
    for i in range(1, pageNum + 1):
        url = "http://m.maoyan.com/mmdb/comments/movie/1203084.json?_v_=yes&offset=%d" % i

        save_to_txt(url)
