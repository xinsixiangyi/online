
import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewBegin.settings")

import django
django.setup()

from my_blogs.models import Blogs,BlogsCategory

from db_tools.data.blogs_data import categorys_data,blog_data
for blogs_detail in blog_data:
    blogs = Blogs()
    blogs.name = blogs_detail["name"]
    #前端中是“￥232”，数据库中是float类型，所以要替换掉

    blogs.click_num= blogs_detail["content"]['click_num'] if blogs_detail["content"]['click_num'] is not None else ""
    blogs.star_num = blogs_detail["content"]['star_num'] if blogs_detail["content"]['star_num'] is not None else ""
    blogs.fav_num= blogs_detail["content"]['fav_num'] if blogs_detail["content"]['fav_num'] is not None else ""
    blogs.blog_path = blogs_detail["content"]['blog_path'] if blogs_detail["content"]['blog_path'] is not None else ""
    blogs.add_time = blogs_detail["content"]['add_time'] if blogs_detail["content"]['add_time'] is not None else ""
    blogs.modify_time = blogs_detail["content"]['modify_time'] if blogs_detail["content"]['modify_time'] is not None else ""
    blogs.access_time = blogs_detail["content"]['access_time'] if blogs_detail["content"]['access_time'] is not None else ""
    # blogs.blogs_desc = blogs_detail["blogs_desc"] if blogs_detail["blogs_desc"] is not None else ""
    # # 取第一张作为封面图
    # blogs.blogs_front_image = blogs_detail["images"][0] if blogs_detail["images"] else ""
    #取最后一个
    category_name = blogs_detail["content"]["categorys"][-1]
    # 取出当前子类对应的blogsCategory对象，filter没有匹配的会返回空数组，不会抛异常。
    print(category_name)
    category = BlogsCategory.objects.filter(name=category_name)
    if category:
        blogs.category = category[0]
    blogs.save()