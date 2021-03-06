# Generated by Django 2.2.16 on 2021-05-24 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0005_auto_20210409_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogContents', models.TextField(blank=True, db_column='AssentPorts', verbose_name='博客内容')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='最后修改时间')),
            ],
            options={
                'db_table': 'Blog_Contents',
            },
        ),
    ]
