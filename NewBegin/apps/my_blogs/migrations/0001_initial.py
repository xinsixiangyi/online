# Generated by Django 2.2.16 on 2020-12-14 15:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('desc', models.TextField(default='', help_text='类别描述', verbose_name='类别描述')),
                ('category_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类目级别', verbose_name='类目级别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='my_blogs.BlogsCategory', verbose_name='父类别')),
            ],
            options={
                'verbose_name': '博客类别',
                'verbose_name_plural': '博客类别',
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300, verbose_name='博客名')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('star_num', models.IntegerField(default=0, verbose_name='点赞量')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('blog_path', models.CharField(default='', max_length=300, verbose_name='博客路径')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='最后修改时间')),
                ('access_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='最后访问时间')),
                ('creat_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_blogs.BlogsCategory', verbose_name='博客类目')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
            },
        ),
    ]
