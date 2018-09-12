# -*- coding:utf-8 -*-
'''
@time   : 2018-08-15 10:29
@author : Zephyr
@file   : 04beautifulsoup.py
'''
from bs4 import BeautifulSoup
import re

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p class="sister">
    <b>The Dormouse's story</b>
    <i> this is p.i</i>
</p>
<div>
<p class="title">
    <b>The Dormouse's story</b>
    <i> this is p.i</i>
</p>
</div>

<p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="brother" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
'''
# 格式化
print(soup.prettify())

# 标签名
print(soup.title)

print(soup.p)
# 能连用
print(soup.p.b)
# .name 标签名
print(soup.title.name)
# .attrs 属性字典{'属性名' : []}
print(soup.p.attrs['class'])
# 获取标签下所有文本
print(soup.p.text)
print(soup.p.get_text())
# 获取当前标签下文本
print(soup.p.string)
'''
# print(soup.p['class'])

# print(soup.title.parent)
# print(soup.title.parents)
# print(soup.p.next_sibling.next_sibling)
'''
name=None,  标签名
attrs={},  属性
recursive=True,  追踪 
text=None, 文本 
limit=None 限制输出
'''
# 返回一个列表 所有
# print(soup.find_all('p'))
# # # 只找到第一个
# # print(soup.find('p'))
# #
# # # 正则
# # # 以E开头的文本
# # print(soup.find_all(text=re.compile('^L')))
# # # class=sister
# # print(soup.find_all('a', attrs={'class': 'sister'}))
# # print(soup.find_all(class_='sister'))
# # print(soup.find_all(id='link2'))
# class=sister & brother
# 或操作 []
print(soup.find_all('a', class_=['sister', 'brother'], limit=1))
# class = sister
# 返回列表
print(soup.select('.sister'))
print('*'*20)
print(soup.select('a.sister'))
