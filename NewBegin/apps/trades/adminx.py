# -*- coding: utf-8 -*-
__author__ = 'bobby'

import xadmin
from .models import ShoppingCart, OrderInfo, OrderGoods

class OrderInfoAdmin(object):
    list_display = ["user", "order_sn",  "trade_no", "pay_status", "post_script", "order_mount", "order_mount", "pay_time", "add_time"]
    model_icon = 'fa fa-money'
    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]

class ShoppingCartAdmin(object):
    list_display = ["user", "goods", "nums", ]

    model_icon = 'fa fa-shopping-cart'
xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
