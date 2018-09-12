from django.db import models

# Create your models here.
# axf_wheel(img, name, trackid)

class BaseData(models.Model):
    img = models.CharField(
        max_length=255,
        verbose_name="图片"
    )
    name = models.CharField(
        max_length=100
    )
    trackid = models.CharField(
        max_length=50
    )
    class Meta:
        abstract = True

class MyWheel(BaseData):

    class Meta:
        db_table = "axf_wheel"
        verbose_name = "轮播数据"

class MyNav(BaseData):

    class Meta:
        db_table = "axf_nav"
        verbose_name = "导航数据"


class MustBuy(BaseData):

    class Meta:
        db_table = "axf_mustbuy"
        verbose_name = "必购"

class MyShop(BaseData):

    class Meta:
        db_table = "axf_shop"
        verbose_name = "商店"


class MainShow(models.Model):
    trackid = models.CharField(
        max_length=200
    )
    name = models.CharField(
        max_length=200
    )
    img = models.CharField(
        max_length=200
    )
    categoryid = models.CharField(
        max_length=200
    )
    brandname = models.CharField(
        max_length=200
    )
    img1 = models.CharField(
        max_length=200
    )
    childcid1 = models.CharField(
        max_length=200
    )
    productid1 = models.CharField(
        max_length=200
    )
    longname1 = models.CharField(
        max_length=200
    )
    price1 = models.CharField(
        max_length=200
    )
    marketprice1 = models.CharField(
        max_length=200
    )
    img2 = models.CharField(
        max_length=200
    )
    childcid2 = models.CharField(
        max_length=200
    )
    productid2 = models.CharField(
        max_length=200
    )
    longname2 = models.CharField(
        max_length=200
    )
    price2 = models.CharField(
        max_length=200
    )
    marketprice2 = models.CharField(
        max_length=200
    )
    img3 = models.CharField(
        max_length=200
    )
    childcid3 = models.CharField(
        max_length=200
    )
    productid3 = models.CharField(
        max_length=200
    )
    longname3 = models.CharField(
        max_length=200
    )
    price3 = models.CharField(
        max_length=200
    )
    marketprice3 = models.CharField(
        max_length=200
    )


class GoodsType(models.Model):
    typeid = models.CharField(
        max_length=20
    )
    typename = models.CharField(
        max_length=30
    )
    childtypenames = models.CharField(
        max_length=255
    )
    typesort = models.IntegerField()

    class Meta:
        db_table = "axf_foodtypes"
        verbose_name = "商品分类"


class Goods(models.Model):
    productid = models.CharField(
        max_length=10
    )
    productimg = models.CharField(
        max_length=200
    )
    productname = models.CharField(
        max_length=100
    )
    productlongname = models.CharField(
        max_length=255
    )
    isxf = models.BooleanField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(
        max_length=50
    )
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(
        max_length=100
    )
    dealerid = models.CharField(
        max_length=30
    )
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = "axf_goods"