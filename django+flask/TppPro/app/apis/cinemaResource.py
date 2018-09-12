# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/8 14:41
@Author  : Fate
@File    : cinemaResource.py
'''

from flask_restful import Resource, fields, marshal_with, reqparse
from app.models.cinemaModel import Cinema

cinema_fields = {
    "id": fields.Integer,
    # 影院名
    "name": fields.String,
    # 城市
    "city": fields.String,
    # 区
    "district": fields.String,
    # 地址
    "address": fields.String,
    # 电话
    "phone": fields.String,
    # 评分
    "score": fields.Float,
    # 放映厅数量
    "hallnum": fields.Integer,
    # 服务费
    "servicecharge": fields.Float,

    "astrict": fields.Integer,
    # 标记
    "flag": fields.Boolean,
    # 是否下架
    "isdelete": fields.Boolean,

}

result_value = {
    'msg': fields.String,
    'status': fields.Integer,
    'data': fields.List(fields.Nested(cinema_fields))
}

# 按分区查找
parser = reqparse.RequestParser()
parser.add_argument('district', type=str)


class CinemaResource(Resource):
    @marshal_with(result_value)
    def get(self):
        args = parser.parse_args()

        # 分区
        district = args.get('district')
        if district:
            # and 可连写 .filter_by(city=city).filter_by(district=district)

            cinemas = Cinema.query.filter_by(district=district)
        else:
            cinemas = Cinema.query.all()

        return {
            'msg': '影院查找成功',
            'status': 200,
            'data': cinemas
        }
