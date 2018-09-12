from django.shortcuts import render
from .models import *

# Create your views here.

def home(req):
    # 拿轮播数据
    swipers = MyWheel.objects.raw("SELECT * FROM axf_wheel")
    # 拿导航数据
    navs = MyNav.objects.all()
    # 拿必购的数据
    mustbys = MustBuy.objects.all()
    # 拿商店数据
    shops = MyShop.objects.all()
    shop_img = shops[0]
    # 拿商品数据
    goods = MainShow.objects.all()
    data = {
        'title': '首页',
        'swipers': swipers,
        'navs': navs,
        'must_bys': mustbys,
        'shop_img': shop_img,
        'shop_two': shops[1:3],
        'shop_more': shops[3:7],
        'shop_last': shops[7:],
        'goods': goods
    }
    return render(req, 'home/home.html', data)

def market(req, type_id, sub_type_id ):
    # 拿全部的分类数据
    all_types = GoodsType.objects.all()


    # 拿商品
    goods = Goods.objects.filter(categoryid=type_id)
    # 如果二级分类的id不得0 那就需要在原有数据集goods的基础上 找对应二级分类对应的数据
    if int(sub_type_id) != 0:
        goods = goods.filter(childcid=sub_type_id)


    # t通过查询出来的数据集找到选中的那个分类数据
    select_type = all_types.get(typeid=type_id)

    # 拿到二级分类数据
    all_sub_type = select_type.childtypenames
    type_name_id_list = all_sub_type.split("#") #将子分类数据切分
    # 低端写法
    # sub_types = []
    # for i in type_name_id_list:
    #     name_ids = i.split(":")
    #     sub_types.append(name_ids)
    sub_types = [ i.split(':') for i in type_name_id_list]
    # print(sub_types)
    data = {
        'title': '闪购',
        'types': all_types,
        'goods': goods,
        'selected_typeid': type_id,
        'sub_types': sub_types,
        'select_sub_type_id': sub_type_id
    }
    return render(req, 'market/market.html', data)

def cart(req):
    data = {
        'title': '购物车'
    }
    return render(req, 'cart/cart.html', data)

def mine(req):
    data = {
        'title': '我的'
    }
    return render(req, 'mine/mine.html', data)