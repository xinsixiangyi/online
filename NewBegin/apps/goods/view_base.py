#_*_coding:utf-8_*_
'''
===================================
	view_base.py.py
	======================
	@descript: 

	@copyright:Topsec
	@author:xfjing
	@date:2020/10/29   15:33
===========================================
'''
from django.views.generic import View
from goods.models import Goods
class GoodsListView(View):
	def get(self,request):
		#通过django的view实现商品列表页
		json_list = []
		#获取所有商品
		goods = Goods.objects.all()
		# print(goods)
		# for good in goods:
		# 	json_dict = {}
		# 	# 获取商品的每个字段，键值对形式
		# 	json_dict['name'] = good.name
		# 	json_dict['category'] = good.category.name
		# 	json_dict['market_price'] = good.market_price
		# 	json_list.append(json_dict)
		# from django.forms.models import model_to_dict
		# for good in goods:
		# 	json_dict = model_to_dict(good)
		# 	print(json_dict)
		# 	json_list.append(json_dict)
		from django.http import HttpResponse,JsonResponse
		import json
		from django.core import serializers
		json_data = serializers.serialize('json', goods)
		json_data = json.loads(json_data)
		# 返回json，一定要指定类型content_type='application/json'
		# return HttpResponse(json.dumps(json_list), content_type='application/json')
		return JsonResponse(json_data, safe=False)
