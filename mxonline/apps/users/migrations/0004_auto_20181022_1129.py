# Generated by Django 2.1.2 on 2018-10-22 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181020_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=10, verbose_name='发送类型'),
        ),
    ]