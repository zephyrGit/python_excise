# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/8 14:04
@Author  : Fate
@File    : cinemaModel.py 影院数据模型
'''

from app.extensions import db

'''
insert into cinemas(name,city,district,address,phone,
score,hallnum,servicecharge,
astrict,flag,isdelete)
values("深圳戏院影城","深圳","罗湖","罗湖区新园路1号东门步行街西口",
"0755-82175808",9.7,9,1.2,20,1,0);
'''


# 主
# 主-->备
# 主+备 -->从
class Cinema(db.Model):
    __tablename__ = 'cinemas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 影院名
    name = db.Column(db.String(64))
    # 城市
    city = db.Column(db.String(32))
    # 区
    district = db.Column(db.String(32))
    # 地址
    address = db.Column(db.String(255))
    # 电话
    phone = db.Column(db.String(32))
    # 评分
    score = db.Column(db.Float, default=10)
    # 放映厅数量
    hallnum = db.Column(db.Integer, default=1)
    # 服务费
    servicecharge = db.Column(db.Float, default=0)

    astrict = db.Column(db.Integer, default=1)
    # 标记
    flag = db.Column(db.Boolean, default=True)
    # 是否下架
    isdelete = db.Column(db.Boolean, default=False)
