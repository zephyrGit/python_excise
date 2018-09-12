# -*- coding:utf-8 -*-
'''
@time   : 2018-08-15 16:18
@author : Zephyr
@file   : 08插入数据库.py
'''
import pymysql

connect = pymysql.connect(host='127.0.0.1', user='root', password="5214",
                          database='tx', port=3306, charset='utf8')

# 游标
cur = connect.cursor()

# 读取
with open('tencent.txt', 'r', errors='ignore', encoding='utf-8') as f:
    jobList = f.readlines()
    for job in jobList:
        job = eval(job)
        sql = "INSERT INTO tencent(jobName, jobUrl, jobType, jobNum, jobAddr, jobTime) VALUES " \
              "(%r,%r,%r,%r,%r,%r)" % (job[0], job[1], job[2], job[3], job[4], job[5])
        print(job)
        print(sql)
        cur.execute(sql)
        connect.commit()

cur.close()
connect.close()
