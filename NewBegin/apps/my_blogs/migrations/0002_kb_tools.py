# Generated by Django 2.2.16 on 2021-01-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kb_tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toolname', models.CharField(blank=True, db_column='ToolName', max_length=64)),
                ('toolaccount', models.CharField(blank=True, db_column='ToolAccount', max_length=64)),
                ('toolpassword', models.CharField(blank=True, db_column='ToolPassword', max_length=64)),
                ('tooladress', models.CharField(blank=True, db_column='ToolAdress', max_length=64)),
                ('adressaccount', models.CharField(blank=True, db_column='AdressAccount', max_length=64)),
                ('adresspassword', models.CharField(blank=True, db_column='AdressPassword', max_length=64)),
                ('modifytime', models.DateTimeField(auto_now=True, db_column='ModifyTime')),
                ('addtime', models.DateTimeField(auto_now_add=True, db_column='AddTime')),
                ('data', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'kb_tools',
            },
        ),
    ]
