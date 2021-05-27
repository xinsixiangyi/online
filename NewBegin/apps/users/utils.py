#_*_coding:utf-8_*_
'''
===================================
	utils.py.py
	======================
	@descript:

	@copyright:Topsec
	@author:xfjing
	@date:2020/12/18   15:35
===========================================
'''

import base64,json
"""引入simple登陆验证成功的模块"""
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
"""引入simple登陆验证失败的模块"""
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework.views import APIView
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	"自定义令牌签名内容"
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		# Add custom claims
		token['name'] = user.username,
		# ...
		return token


	"自定义登陆正确返回方法"
	def validate(self, attrs):
		data = super().validate(attrs)
		refresh = self.get_token(self.user)

		data.pop("refresh")
		data.pop('access')
		data.update({"code":200})
		data["msg"]="success"
		# data["code"] = "200",
		data["data"]={
			'username':self.user.username,
			'accessToken':str(refresh.access_token),
			'refresh':str(refresh)
		}
		return data
class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer

class JwtDecode():
	def __init__(self,authenticated):
		self.jwt_header = authenticated.split(".")[0].split(" ")[1]
		self.jwt_payload=authenticated.split(".")[1]
		pass
	def get_jwt_header(self):
		jwt_header = base64.b64decode(self.jwt_header+"=").decode("utf-8")
		return json.loads(jwt_header)
	def get_jwt_payload(self):
		jwt_payload = base64.b64decode(self.jwt_payload + "=").decode("utf-8")
		return json.loads(jwt_payload)
	pass