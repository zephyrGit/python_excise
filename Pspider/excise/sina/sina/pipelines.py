# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class SinaPipeline(object):

    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    user='root',
                                    password="5214",
                                    database='mysina',
                                    port=3306,
                                    charset='utf8')

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO sina(newsTitle, newsUrl, newsTime, newsContent)" \
              " VALUES (%r,%r,%r,%r)" % (item['newsTitle'], item['newsUrl'],
                                         item['newsTime'], item['newsContent'])

        print(sql)

        self.cur.execute(sql)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
