# Generated by Django 2.2.16 on 2020-10-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='nonce_str',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='随机加密串'),
        ),
    ]
