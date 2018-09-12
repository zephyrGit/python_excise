# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/7 9:10
@Author  : Fate
@File    : cityResource.py 城市api
'''

from flask_restful import Resource, fields, marshal_with, marshal
from app.models import City, Letter


'''
{
  "returnCode": "0",
  "returnValue": {
    "A": [
      {
        "id": 3643,
        "parentId": 0,
        "regionName": "阿坝",
        "cityCode": 513200,
        "pinYin": "ABA"
      },]
    }
}
'''

# 城市
city_fields = {
    "id": fields.Integer,
    "regionName": fields.String,
    "cityCode": fields.Integer,
    "pinYin": fields.String
}
# 字母
letter_fields = {
    "A": fields.List(fields.Nested(city_fields)),
    "B": fields.List(fields.Nested(city_fields)),
    "C": fields.List(fields.Nested(city_fields))
}
# 返回结果
result_value_fields = {
    "returnCode": fields.String,
    "returnValue": fields.Nested(letter_fields)
}


# 定义城市资源

class CityResource(Resource):
    # 显示城市
    @marshal_with(result_value_fields)
    def get(self):
        # 返回城市
        result_value = {}
        # cities = City.query.all()
        # 所有的字母
        letters = Letter.query.all()

        for letter in letters:
            # 通过字母查找对应城市
            city = City.query.filter_by(letter_id=letter.id)
            result_value[letter.letter] = city

        return {
            "returnCode": "0",
            "returnValue": result_value
        }

    def post(self):
        # 返回城市结果
        result_value = {}
        # cities = City.query.all()
        # 所有的字母
        letters = Letter.query.all()
        # 存放字母 动态的
        letter_fields_dynamic = {}

        for letter in letters:
            # 通过字母查找对应城市
            city = City.query.filter_by(letter_id=letter.id)

            # 按字典格式，填入值{"字母"：[{城市}]}}
            letter_fields_dynamic[letter.letter] = fields.List(fields.Nested(city_fields))
            # {"字母"："城市值"}
            result_value[letter.letter] = city

            # 返回给前端
            result_value_dynamic = {
                "returnCode": fields.String,
                "returnValue": fields.Nested(letter_fields_dynamic)
            }

        result = marshal({
            "returnCode": "0",
            "returnValue": result_value
        }, fields=result_value_dynamic)

        return result
