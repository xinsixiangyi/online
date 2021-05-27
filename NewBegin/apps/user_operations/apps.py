from django.apps import AppConfig


class UserOperationsConfig(AppConfig):
    name = 'user_operations'
#app名字后台显示中文
    verbose_name = "操作管理"
    orederIndex = 4