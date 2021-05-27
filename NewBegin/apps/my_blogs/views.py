from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from my_blogs.serializers import BlogsSerializer,CategorySerializer
from .models import Blogs,BlogsCategory,Blog_Contents
from rest_framework.response import Response
from rest_framework import mixins,serializers
from rest_framework import generics,viewsets
from rest_framework.pagination import PageNumberPagination
from .filters import BlogsFilter
from .note_sort import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.conf import settings
class BlogsPagination(PageNumberPagination):
	'''
	博客列表自定义分页
	'''
	#默认每页显示的个数
	page_size = 10
	#可以动态改变每页显示的个数
	page_size_query_param = 'page_size'
	#页码参数
	page_query_param = 'page'
	#最多能显示多少页
	max_page_size = 100
class BlogsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
	'博客列表页'

	# 这里必须要定义一个默认的排序,否则会报错
	queryset = Blogs.objects.all().order_by("creat_time")
	# 分页
	pagination_class = BlogsPagination
	# 序列化
	serializer_class =BlogsSerializer
	filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

	# 设置filter的类为我们自定义的类
	# 过滤
	filter_class = BlogsFilter
class BlogsCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
	'''
	list:
		博客分类列表数据
	'''
	queryset = BlogsCategory.objects.filter(category_type=1)
	serializer_class = CategorySerializer

# class BlogsContents(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
# 	'''
# 	list:
# 		博客内容
# 	'''
# 	queryset =blogData()
# 	serializer_class = CategorySerializer

class BlogsContents(APIView):
	'''
	# 	list:
	# 		博客内容
	# 	'''
	def get(self,request): # 请求为get时的业务逻辑
		# """业务逻辑"""
		blog_path=os.path.join(settings.FRONT_ROOT, 'public/blog_store/posts')
		queryset = blogData(blog_path)
		file_path = os.path.join(settings.FRONT_ROOT, "public/blog_store/posts_index.json")
		#获取数据库最后一条数据
		contents= Blog_Contents.objects.all().last()
		if contents.BlogContents!=queryset:
			Blog_Contents.objects.create(BlogContents=queryset)
			with open(file_path, 'w',encoding='utf-8') as file_to_read:
				file_to_read.writelines(queryset)
		# return HttpResponse(json.dumps(queryset), content_type="application/json")
		return HttpResponse('ok')
	# def post(self,request): # 请求为post时的业务逻辑
	# 	"""业务逻辑"""
	# 	message={}
	# 	form_body = request.data
	# 	print(form_body)
	# 	return Response(message)

