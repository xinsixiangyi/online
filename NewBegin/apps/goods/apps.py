from django.apps import AppConfig


class GoodsConfig(AppConfig):
    name = 'goods'
    #app名字后台显示中文
    verbose_name = "商品管理"
    orederIndex = 2