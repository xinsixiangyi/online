# db_tools/data/import_category_data.py


# 独立使用django的model
import sys
import os
#  获取当前文件的路径，以及路径的父级文件夹名
pwd = os.path.dirname(os.path.realpath(__file__))
# 将项目目录加入setting
sys.path.append(pwd + "../")
# manage.py中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewBegin.settings")

import django
django.setup()

# 这行代码必须在初始化django之后
from my_blogs.models import BlogsCategory

from db_tools.data.blogs_data import categorys_data

# 一级分类
for lev1_cat in categorys_data:
    lev1_intance = BlogsCategory()
    lev1_intance.name = lev1_cat["name"]
    lev1_intance.category_type = 1
    lev1_intance.save()

    #二级分类
    if lev1_cat.get('sub_categorys'):
        for lev2_cat in lev1_cat["sub_categorys"]:
            lev2_intance =  BlogsCategory()
            lev2_intance.name = lev2_cat["name"]
            lev2_intance.category_type = 2
            lev2_intance.parent_category = lev1_intance
            lev2_intance.save()

            #三级分类
            if lev2_cat.get('sub_categorys'):
                for lev3_cat in lev2_cat["sub_categorys"]:
                    lev3_intance = BlogsCategory()
                    lev3_intance.name = lev3_cat["name"]
                    lev3_intance.category_type = 3
                    lev3_intance.parent_category = lev2_intance
                    lev3_intance.save()
    print('目录保存成功')
