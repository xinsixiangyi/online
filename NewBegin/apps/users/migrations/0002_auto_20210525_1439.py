# Generated by Django 2.2.16 on 2021-05-25 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='mobile',
            new_name='mobicle',
        ),
    ]
