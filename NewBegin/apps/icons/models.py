from django.db import models

# Create your models here.
class Icons(models.Model):
	"""
	所有图标
	"""
	CATEGORY_TYPE = (

		(1, "常规图标"),

		(2, "未定义2"),

		(3, "未定义3"),

	)
	icons_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="图标分类")
	name = models.CharField(max_length=300, default="", verbose_name="图标名")

	class Meta:

		verbose_name = "图标"

		verbose_name_plural = verbose_name

	def __str__(self):

		return str(self.name)
