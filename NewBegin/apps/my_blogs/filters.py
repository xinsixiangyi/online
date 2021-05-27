#_*_coding:utf-8_*_
'''
===================================
	filters.py.py
	======================
	@descript: 

	@copyright:Topsec
	@author:xfjing
	@date:2020/10/31   14:07
===========================================
'''
import django_filters
from .models import Blogs

class BlogsFilter(django_filters.rest_framework.FilterSet):
	'''
	博客过滤的类
	'''
	#  iexact表示精确匹配, 并且忽略大小写， #icontains表示模糊查询（包含），并且忽略大小写
	search_field = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
	ordering = django_filters.OrderingFilter(fields=('click_num','star_num','fav_num', 'add_time'),
											 field_labels={'click_num': '点击数', 'star_num':'点赞数','fav_num':'收藏数','add_time': '添加时间'})

	class Meta:
		model = Blogs
		fields = ['search_field']