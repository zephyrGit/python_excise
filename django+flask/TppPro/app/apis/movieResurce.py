# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/8 10:57
@Author  : Fate
@File    : movieResurce.py
'''

from flask_restful import Resource, fields, marshal_with, reqparse
from app.models import Movie

movie_fields = {
    "id": fields.Integer,
    # 电影，名
    "showname": fields.String,
    # 英文名
    "shownameen": fields.String,
    # 导演
    "director": fields.String,
    # 主演
    "leadingRole": fields.String,
    # 电影类型
    "type": fields.String,
    # 国家
    "country": fields.String,
    # 语言
    "language": fields.String,
    # 片长
    "duration": fields.Integer,
    # 放映方式
    "screeningmodel": fields.String,
    # 首映
    "openday": fields.DateTime,
    # 海报
    "backgroundpicture": fields.String,
    # 标记
    "flag": fields.Integer,
    # 是否下架
    "isdelete": fields.Boolean
}
result_value = {
    'msg': fields.String,
    'status': fields.Integer,
    'data': fields.List(fields.Nested(movie_fields))
}

parser = reqparse.RequestParser()
parser.add_argument('director', type=str)



class MovieResource(Resource):
    @marshal_with(result_value)
    def get(self):
        # 按导演搜索
        args = parser.parse_args()
        director = args.get('director')
        if director:
            movies = Movie.query.filter_by(director=director)
        else:
            movies = Movie.query.all()
            print(movies)

        return {
            'msg': "电影获取成功",
            'status': 200,
            'data': movies
        }
