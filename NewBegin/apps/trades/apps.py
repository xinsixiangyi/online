from django.apps import AppConfig


class TradesConfig(AppConfig):
    name = 'trades'
#app名字后台显示中文
    verbose_name = "交易管理"
    orederIndex = 3