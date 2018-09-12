# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/7 9:10
@Author  : Fate
@File    : __init__.py.py api
'''

from app.extensions import api
from .cityResource import CityResource
from .userResource import UserResource, ActivationResource, PermissionResource
from .movieResurce import MovieResource
from .cinemaResource import CinemaResource

# 添加城市资源
api.add_resource(CityResource, '/city/')
# 用户
api.add_resource(UserResource, '/user/')
# 激活
api.add_resource(ActivationResource, '/activation/')
# 权限
api.add_resource(PermissionResource, '/permission/')
# 电影
api.add_resource(MovieResource, '/movies/')
# 影院
api.add_resource(CinemaResource, '/cinema/')
