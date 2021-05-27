#_*_coding:utf-8_*_
'''
===================================
serializers.py.py
======================
@descript:

@copyright:Topsec
@author:xfjing
@date:2020/10/30   11:22
===========================================
'''
# goods/serializers.py

from rest_framework import serializers
#drf自定义序列化器
#class GoodsSerializer(serializers.Serializer):
#	name = serializers.CharField(required=True,max_length=100)
#	click_num = serializers.IntegerField(default=0)
#	goods_front_image = serializers.ImageField()
from .models import Blogs,BlogsCategory
# class CategorySerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = BlogsCategory
# 		fields = "__all__"


class CategorySerializer3(serializers.ModelSerializer):
	'''三级分类'''
	class Meta:
		model = BlogsCategory
		fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
	'''
	二级分类
	'''
	#在parent_category字段中定义的related_name="sub_cat"
	sub_cat = CategorySerializer3(many=True)
	class Meta:
		model =BlogsCategory
		fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
	"""
	商品一级类别序列化
	"""
	sub_cat = CategorySerializer2(many=True)
	class Meta:
		model = BlogsCategory
		fields = "__all__"


# drf序列化博客所有信息，ModelSerializer实现商品列表页
class BlogsSerializer(serializers.ModelSerializer):
	# 覆盖外键字段
	category = CategorySerializer()
	class Meta:
		model = Blogs
		fields = '__all__'
