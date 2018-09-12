# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 14:49
@author : Zephyr
@file   : 10分词.py
'''

import jieba

str = '你TMD比新四军129师386旅独立团团长李云龙他老婆秀琴还秀'
str1 = '你TMD比新四军129师386旅独立团团长李云龙他老婆秀琴还秀'

mycut = jieba.cut_for_search(str)  # 按搜索引擎搜索

cutStr = jieba.cut(str1, cut_all=True)
# print(mycut)  # generator

# for i in mycut:
#     print(i)

print('/'.join(mycut))
print('*'.join(cutStr))

