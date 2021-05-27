from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from users.utils import JwtDecode
from users.models import UserProfile
from rest_framework.views import APIView,Response

# 记得引入用户的model
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # noinspection PyBroadException
        try:
            # 小编这里添加了一个手机验证，如果需要其他验证再加就ok了
            user = UserProfile.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class Aa(APIView):
    # def get(self,request): # 请求为get时的业务逻辑
    #     """业务逻辑"""
    #
    #     return XXXXX
    def post(self,request): # 请求为post时的业务逻辑
        """业务逻辑"""
        message={}
        form_body = request.data
        print(form_body)
        return Response(message)

class UsersInfo(APIView):
    # def get(self,request): # 请求为get时的业务逻辑
    #     """业务逻辑"""
    #
    #     return XXXXX
    # 标记需要进行jwt验证
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)
    def post(self,request): # 请求为post时的业务逻辑
        """业务逻辑"""
        message={
        "code": 200,
        "msg": 'success',
        "data": {}}
        #获取前端返回的jwt令牌
        jwt_token = request.META.get("HTTP_AUTHORIZATION")
        #解码
        payload =JwtDecode(jwt_token).get_jwt_payload()
        # form_body = request.data
        #
        # print(form_body["accessToken"])
        if payload["name"][0]=="admin":
            message["data"].update({"roles" : ['admin']})
            message["data"].update({"ability" : ['READ']})
            message["data"].update({"username" : payload["name"][0]})
            message["data"].update( {'avatar':
            'https://api.sunweihu.com/api/sjtx/api.php?lx=c1',
          })
        else:
            message["data"].update({"roles": ['admin', 'editor']})
            message["data"].update({"ability": ['READ']})
            message["data"].update({"username": payload["name"][0]})
            message["data"].update({'avatar':
            'https://api.sunweihu.com/api/sjtx/api.php?lx=c1',
          })
        return Response(message)
class Logout(APIView):
    # def get(self,request): # 请求为get时的业务逻辑
    #     """业务逻辑"""
    #
    #     return XXXXX
    # 标记需要进行jwt验证
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)
    def post(self,request): # 请求为post时的业务逻辑
        """业务逻辑"""
        message={
        "code": 200,
        "msg": 'success',}
        form_body = request.data
        return Response(message)