#_*_coding:utf-8_*_
'''
===================================
	note_sort.py
	======================
	@descript:

	@copyright:Topsec
	@author:xfjing
	@date:2021/5/23   15:24
===========================================
'''
import os,re,random,time,json
from collections import defaultdict
def merge(old_data):
	new_dict = {}
	for i in old_data:
		# print(i.get('sub_categorys'))
		if i.get('sub_categorys') == None:
			new_dict.setdefault(i['name'], [])
		else:
			# print(i.get('sub_categorys'))
			if i.get('sub_categorys'):
				new_dict.setdefault(i['name'], []).append((i.get('sub_categorys'))[0])
			else:
				new_dict.setdefault(i['name'], [])
	# print(new_dict)
	new_list = []
	for x, y in new_dict.items():
		new_list.append({'name': x, 'sub_categorys': y})

	return new_list
'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def TimeStampToTime(timestamp):
	timeStruct = time.localtime(timestamp)
	return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

'''获取文件的大小,结果保留两位小数，单位为MB'''
def get_FileSize(filePath):
	fsize = os.path.getsize(filePath)
	fsize = fsize/float(1024*1024)
	return round(fsize,5)

'''获取文件的访问时间'''
def get_FileAccessTime(filePath):
	t = os.path.getatime(filePath)
	return TimeStampToTime(t)

'''获取文件的创建时间'''
def get_FileCreateTime(filePath):
	t = os.path.getctime(filePath)
	return TimeStampToTime(t)

'''获取文件的修改时间'''
def get_FileModifyTime(filePath):
	t = os.path.getmtime(filePath)
	return TimeStampToTime(t)


def fileMessage(dirlist):

	for i in dirlist:
		# print(get_FileModifyTime(i))
		return  get_FileModifyTime(i),get_FileCreateTime(i),get_FileAccessTime(i)

	# print("获取文件的创建时间")
	# for i in dirlist:
	#     print(get_FileCreateTime(i))
	#
	# print("获取文件的访问时间")
	# for i in dirlist:
	#     print(get_FileAccessTime(i))
def blogData(file_path):
	# base_path='/opt/blogcontent/Study-notes'
	# print(os.path.abspath("blogs_data_test.py"))
	# print(os.listdir('D:/git/NewBegin/media/blogs/notebook'))
	row_data = [ ]
	blog_datas = []
	categorys_data = []
	for root, dirs, files in os.walk(file_path, topdown=False):
		# print(root)
		for name in files:
			path=os.path.join(root, name)
			standard_path=path.replace('\\','/')

			modify_time,add_time,access_time=fileMessage([standard_path])
			click_num=random.randint(3,1000)
			star_num=random.randint(2,click_num-1)
			fav_num=random.randint(1,star_num-1)

			blog_path=root.replace('\\','/').replace(file_path,'')
			if re.search('\.git',blog_path):
				pass
			else:
				categorys =[ blog_path.split('/')[-1]]
				# print(categorys)
				list = os.listdir(root)  # 列出文件夹下所有的目录与文件
				for i in list:
					if re.search('md',i):
						pass
					else:
						categorys.append('通用知识')
						break

				# categorys=blog_path.split('/')[1:]
				if categorys:
					pass
				else:
					categorys='通用知识'

				with open(standard_path, 'r',encoding='utf8') as file_to_read:
					description=file_to_read.read(150)
				description=description.replace('\n','').replace('\t','')
				row_dict = {"name": '',
							"content": {"click_num": '',
										"star_num": '',
										"fav_num": '',
										"blog_path": '',
										"add_time": '',
										"modify_time": '',
										"access_time": '',
										"categorys":''
										}}

				blog_data={
		"id": "",
		"section": "",
		"date": "",
		"title": "",
		"description": "",
		"url": "blog_store/posts/"
	}


				row_dict["name"]=name
				row_dict["content"]["modify_time"] =modify_time
				row_dict["content"]["add_time"] = add_time
				row_dict["content"]["access_time"] = access_time
				row_dict["content"]["click_num"]= click_num
				row_dict["content"]["star_num"] = star_num
				row_dict["content"]["fav_num"]=fav_num
				row_dict["content"]["blog_path"] = standard_path
				row_dict["content"]["categorys"] = categorys
				row_data.append(row_dict)
				blog_data["id"]=name
				blog_data["section"] = categorys[0]
				blog_data["date"] =modify_time
				blog_data["title"] = name
				blog_data["description"] = description
				blog_data["url"] = blog_data["url"]+categorys[0]+"/"+name
				blog_datas.append(blog_data)





			categorys_dict = {}
			if blog_path:
				categorys_ONE=blog_path.split('/')[1:]

				if '.git' not in categorys_ONE:
					list = os.listdir(root)  # 列出文件夹下所有的目录与文件
					for i in list:
						if re.search('md', i):
							pass
						else:
							categorys_ONE.append('通用知识')
							break
					for x in range(len(categorys_ONE)):

						if x==0 :
							categorys_dict.update({"name":categorys_ONE[x],"sub_categorys":[]})
						elif x==1:
							categorys_dict["sub_categorys"].append({"name":categorys_ONE[x],"sub_categorys":[]})

						elif x==2:
							# print(categorys_dict)
							categorys_dict["sub_categorys"][0]["sub_categorys"]=[{"name":categorys_ONE[x],"sub_categorys":[]}]
						# categorys_dict["sub_categorys"]["sub_categorys"]['name']= categorys_ONE[x]

					categorys_data.append(categorys_dict)
				else:
					categorys_dict.update({'name':"通用知识"})
					categorys_data.append(categorys_dict)
					# print(categorys_ONE)
					# print(re.search('/',categorys_ONE))

					# print(categorys_ONE)
	ww=[]
	for x in categorys_data:
		if x not in ww :
			ww.append(x)
	new_list = merge(ww)
	index = 0
	for k in new_list:

		# print(k.get('sub_categorys'))
		if k.get('sub_categorys'):
			m = merge(k.get('sub_categorys'))
			new_list[index]['sub_categorys'] = m
		index += 1
	blog_datas = sorted(blog_datas, key=lambda e: e['date'], reverse=True)
	blog_datas=json.dumps(blog_datas,ensure_ascii=False)
	return blog_datas
	# return json.dumps(blog_datas,ensure_ascii=False)

# for i in new_list:
# 	print(i)


if __name__ == '__main__':
	file_path=r"D:/git/vue3-md-blog-master\public/blog_store/posts"
	blogData(file_path)
	pass