# Generated by Django 2.2.16 on 2021-05-25 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210525_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='mobicle',
            new_name='mobile',
        ),
    ]