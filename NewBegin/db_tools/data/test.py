#_*_coding:utf-8_*_
'''
===================================
	test.py
	======================
	@descript: 

	@copyright:Topsec
	@author:xfjing
	@date:2020/12/11   17:28
===========================================
'''
a="eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjEwMDkzNDg0LCJqdGkiOiIxZjBjM2VlYzVkY2Q0Y2NmODJkOTM4ZGYzOGExNDM0NSIsInVzZXJfaWQiOjEsIm5hbWUiOlsiYWRtaW4iXX0="
import base64
url = "aHR0cHM6Ly93d3cuY25ibG9ncy5jb20vc29uZ3poaXh1ZS8="
str_url = base64.b64decode(a).decode("utf-8")
print(str_url)
if __name__ == '__main__':
	pass