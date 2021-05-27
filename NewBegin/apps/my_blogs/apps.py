from django.apps import AppConfig


# class MyBlogsConfig(AppConfig):
#     name = 'my_blogs'
class  MyBlogsConfig(AppConfig):
    name = 'my_blogs'
    #app名字后台显示中文
    verbose_name = "博客管理"
    orederIndex = 1