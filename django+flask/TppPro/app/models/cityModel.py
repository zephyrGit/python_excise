# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 14:50
@Author  : Fate
@File    : cityModel.py 城市数据模型
'''

from app.extensions import db


# 字母
class Letter(db.Model):
    __tablename__ = 'letters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 字母
    letter = db.Column(db.String(2), nullable=False)


# 城市
class City(db.Model):
    # 表名
    __tablename__ = 'cities'
    # id
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    # 城市名
    regionName = db.Column(db.String(32), nullable=False)
    # 城市编号
    cityCode = db.Column(db.Integer, nullable=False)
    # 拼音
    pinYin = db.Column(db.String(32), nullable=False)
    # 字母
    letter_id = db.Column(db.Integer, db.ForeignKey(Letter.id))
