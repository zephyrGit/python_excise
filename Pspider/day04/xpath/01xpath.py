# -*- coding:utf-8 -*-
'''
@time   : 2018-08-16 14:09
@author : Zephyr
@file   : 01xpath.py
'''
import lxml
from lxml import etree

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="ul">
    <ul class="ul">
        <li class="li">1</li>
        <li id="li2">2</li>
        <li class="li">3</li>
    </ul>
</div>

</body>
</html>
'''

# mytree = lxml.etree.parse('./xpath.html') # 读取文件

mytree = lxml.etree.HTML(html)

print(mytree)
# / 从根目录开始 html
print(mytree.xpath('/html/head/title/text()'))

# // 所有
print(mytree.xpath('/html/body/div/ul'))
print(mytree.xpath('//ul'))
# . 当前
ul = mytree.xpath('//ul')[0]

li = ul.xpath('./li')
print(li)

# 谓语  id=2
li2 = mytree.xpath('//li[@id="li2"]')
for li in li2:
    # print(li.text)

    print(li.xpath('./text()'))

l3 = mytree.xpath('//div//li[3]/text()')
print(l3)

li3 = mytree.xpath('//div//li[last()]/text()')
# li3_ = mytree.xpath('//div//li[first()]/text()')
print(li3, '**********')
# print(li3_, '**********')

print(mytree.xpath('//div//li [position() !=2]'))

print(mytree.xpath('//ul[@class="ul"] | //p[@class="ul"]'))