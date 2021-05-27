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
from icons.models import Icons

from db_tools.data.icon_data import row_data

# 一级分类
for lev1_cat in row_data:
    lev1_intance = Icons()
    lev1_intance.name = lev1_cat
    lev1_intance.icons_type = 1
    lev1_intance.save()

print('目录保存成功')
