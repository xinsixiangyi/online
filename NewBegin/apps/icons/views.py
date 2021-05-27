from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from icons.serializers import IconsSerializer
from .models import Icons
from rest_framework.response import Response
from rest_framework import mixins,serializers
from rest_framework import generics,viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
class IconsPagination(PageNumberPagination):
	'''
	博客列表自定义分页
	'''
	#默认每页显示的个数
	page_size = 72
	#可以动态改变每页显示的个数
	page_size_query_param = 'page_size'
	#页码参数
	page_query_param = 'page'
	#最多能显示多少页
	max_page_size = 100
class IconsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
	'图标列表页'

	# 这里必须要定义一个默认的排序,否则会报错
	queryset = Icons.objects.all().order_by("id")
	# 分页
	pagination_class = IconsPagination
	# 序列化
	serializer_class =IconsSerializer


	# 设置filter的类为我们自定义的类
	# 过滤
	# filter_class = BlogsFilter