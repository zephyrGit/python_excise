# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class BaikePipeline(object):
    # 存储到数据库
    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', user='root',
                                    password="5214", database='bdbk',
                                    port=3306, charset='utf8', )

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        # 打包
        # dict(zip([], []))
        row, value = zip(*item.items())

        sql = "INSERT INTO `%s`(%s) VALUES (%s)" \
              % ('baike',
                 ','.join(row),
                 ','.join(['%s'] * len(value))
                 )

        # print(sql, value)
        self.cur.execute(sql, value)
        print(self.cur._last_executed)
        self.conn.commit()

        '''
        1) "mybaike:dupefilter"  指纹 爬取过了的
        2) "mybaike:requests" 请求 待爬取的
        '''
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
