# Generated by Django 2.1.2 on 2018-10-20 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 20, 16, 11, 17, 96592)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 20, 16, 11, 17, 96592)),
        ),
    ]
