# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 16:19
@Author  : Fate
@File    : insertCity.py
'''
import json
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password="123456",
                       database='DevTpp', port=3306,
                       charset='utf8')
# 游标
cursor = conn.cursor()

with open('city.json', 'r', encoding='utf-8') as f:
    # 读取json文件
    city_dict = json.load(f)

    print(city_dict)

    for letter in city_dict['returnValue'].keys():
        # 字母
        print(letter)

        letter_sql = "INSERT INTO letters(letter) VALUES (%r)" % (letter)
        # 开启事务
        try:
            conn.begin()
            # 插入字母
            cursor.execute(letter_sql)
            conn.commit()
        except Exception as e:
            conn.rollback()

        for city in city_dict['returnValue'][letter]:
            # 城市
            # 先 查询 字母的id
            cursor.execute('SELECT id FROM letters WHERE letter="{}"'.format(letter))
            letter_id = cursor.fetchone()[0]
            id = city['id']

            regionName = city['regionName']
            cityCode = city['cityCode']
            pinYin = city['pinYin']
            city_sql = "INSERT INTO cities(id,regionName,cityCode,pinYin,letter_id) " \
                       "VALUES(%d,%r,%d,%r,%d)" % (id, regionName, cityCode, pinYin, letter_id)

            try:
                conn.begin()
                # 插入字母
                cursor.execute(city_sql)
                conn.commit()
            except Exception as e:
                conn.rollback()
            print(city)
