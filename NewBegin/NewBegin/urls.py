"""NewBegin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include,re_path
# Uncomment the next two lines to enable the admin:
from django.views.static import serve
# 导入上传文件目录
from NewBegin.settings import MEDIA_ROOT
import xadmin
xadmin.autodiscover()

#引入semplejwt认证和刷新
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#引入semplejwt认证和刷新
from apps.users import utils
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()
from django.contrib import admin
from goods.views import GoodsListViewSet,CategoryViewSet
from my_blogs.views import BlogsListViewSet,BlogsCategoryViewSet,BlogsContents
from icons.views import IconsListViewSet
from users.views import Aa,UsersInfo,Logout
# from goods.views import GoodsListView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#配置所有商品goods的url
router.register(r'goods/goodlist', GoodsListViewSet, basename="goods")
# 配置商品分类列表Category的url
router.register(r'goods/categoryslist', CategoryViewSet, basename="categorys")
#配置所有博客的url
router.register(r'blogs/bloglist', BlogsListViewSet, basename="blogs")
# 配置博客分类列表Category的url
router.register(r'blogs/categoryslist', BlogsCategoryViewSet, basename="categorys")
# #配置。md博客内容的接口
# router.register(r'blogs/blogcontents', BlogsContents, basename="contents")
# 配置图标列表icons的url
router.register(r'icon/getList', IconsListViewSet, basename="icons")
#测试接口
#users/test



urlpatterns = [
	path('xadmin/', xadmin.site.urls),

	path('ueditor/', include('DjangoUeditor.urls')),
	#文件
	path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
	#商品列表页
    # path('goods/',GoodsListView.as_view(),name='goods-list'),
	#drf文档，title自定义
	path('docs/',include_docs_urls(title='后台rest接口')),
	# jwt的token认证接口
	# path('login/', utils.obtain_jwt_token),
	path('login/', utils.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
	# path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

	path('api-auth/',include('rest_framework.urls')),
	#商品列表页
	re_path('^', include(router.urls)),
	#测试接口
	path('users/test', Aa.as_view()),
	#配置。md博客内容的接口
	path('blogs/blogcontents/', BlogsContents.as_view()),
	path("userInfo/",UsersInfo.as_view()),

	path("logout/",Logout.as_view()),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('index/', include('apps.urls')),
# ]
