# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/8 10:23
@Author  : Fate
@File    : movieModel.py 电影数据模型
'''
from app.extensions import db

'''
insert into movies(id, showname, shownameen,
 director, leadingRole, type, country,
 language, duration, screeningmodel,
  openday, backgroundpicture, flag, isdelete)
  values(228830,"梭哈人生","The Drifting Red Balloon",
  "郑来志","谭佑铭,施予斐,赵韩樱子,孟智超,李林轩",
  "剧情,爱情,喜剧","中国大陆","汉语普通话",90,"4D",
  date("2018-01-30 00:00:00"),"i1/TB19_XCoLDH8KJjy1XcXXcpdXXa_.jpg",1,0);
'''


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    # 电影，名
    showname = db.Column(db.String(64), nullable=False)
    # 英文名
    shownameen = db.Column(db.String(64), nullable=False)
    # 导演
    director = db.Column(db.String(64))
    # 主演
    leadingRole = db.Column(db.String(128))
    # 电影类型
    type = db.Column(db.String(32))
    # 国家
    country = db.Column(db.String(32))
    # 语言
    language = db.Column(db.String(32))
    # 片长
    duration = db.Column(db.Integer)
    # 放映方式
    screeningmodel = db.Column(db.String(10))
    # 首映
    openday = db.Column(db.DateTime)
    # 海报
    backgroundpicture = db.Column(db.String(64))
    # 标记
    flag = db.Column(db.Integer)
    # 是否下架
    isdelete = db.Column(db.Boolean, default=0)





