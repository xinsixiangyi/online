#_*_coding:utf-8_*_
'''
===================================
serializers.py.py
======================
@descript:

@copyright:Topsec
@author:xfjing
@date:2020/12/31   15:36
===========================================
'''
# goods/serializers.py

from rest_framework import serializers
#drf自定义序列化器
#class GoodsSerializer(serializers.Serializer):
#	name = serializers.CharField(required=True,max_length=100)
#	click_num = serializers.IntegerField(default=0)
#	goods_front_image = serializers.ImageField()
from .models import Icons
class IconsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Icons
		fields = "__all__"
