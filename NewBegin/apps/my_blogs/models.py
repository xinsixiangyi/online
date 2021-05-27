from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.
class BlogsCategory(models.Model):

	"""

	博客类别

	"""

	CATEGORY_TYPE = (

		(1, "一级类目"),

		(2, "二级类目"),

		(3, "三级类目"),

	)

	name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")

	desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
	# 目录树级别
	category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
	# 设置models有一个指向自己的外键
	parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类别", related_name="sub_cat",on_delete=models.CASCADE)

	add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

	class Meta:

		verbose_name = "博客类别"

		verbose_name_plural = verbose_name

	def __str__(self):

		return str(self.name)
class Blogs(models.Model):
	"""
	所有博客
	"""
	category = models.ForeignKey(BlogsCategory, verbose_name="博客类目", on_delete=models.CASCADE)
	name = models.CharField(max_length=300, default="", verbose_name="博客名")
	click_num = models.IntegerField(default=0, verbose_name="点击数")
	star_num = models.IntegerField(default=0, verbose_name="点赞量")
	fav_num = models.IntegerField(default=0, verbose_name="收藏数")
	blog_path=models.CharField(max_length=300, default="", verbose_name="博客路径")
	modify_time = models.DateTimeField(default=datetime.now, verbose_name="最后修改时间")
	access_time = models.DateTimeField(default=datetime.now, verbose_name="最后访问时间")
	creat_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
	class Meta:
		verbose_name = "博客"
		verbose_name_plural = verbose_name
	def __str__(self):
		return str(self.name)
class Kb_assents(models.Model):
	assent_hostname= models.CharField(max_length=64, db_column='AssentHostname', blank=True)  # Field name made lowercase.
	assents_ip  = models.CharField(max_length=64, db_column='AssentsIp', blank=True)  # Field name made lowercase.
	assent_mac = models.CharField(max_length=64, db_column='AssentMac', blank=True)  # Field name made lowercase.
	assent_os = models.CharField(max_length=64, db_column='AssentOs', blank=True)  # Field name made lowercase.
	assent_ports = models.TextField(db_column='AssentPorts',blank=True)
	class Meta:
		db_table = 'kb_assents'
class Blog_Contents(models.Model):
	BlogContents = models.TextField(db_column='BlogContents',blank=True,verbose_name="博客内容")
	modify_time = models.DateTimeField(default=datetime.now, verbose_name="最后修改时间")
	class Meta:
		db_table = 'Blog_Contents'