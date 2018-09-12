# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/22 15:05
@Author  : Fate
@File    : 查询sqlachemy.py
'''

from sqlalchemy import create_engine

conn = create_engine("sqlite:///" + r'C:\Users\Administrator\Desktop\spiderPro\IPProxyPool-master\data\proxy.db')

res = conn.execute('select * from proxys')
proxyRes = res.fetchall()
proxyList = []

for i in proxyRes:
    proxy = i[1] + ":" + str(i[2])
    # print(proxy)
    proxyList.append(proxy)

print(proxyList)
