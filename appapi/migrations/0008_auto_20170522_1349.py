# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-22 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0007_auto_20170522_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apicase',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='保存日期'),
        ),
        migrations.AlterField(
            model_name='apicase',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='最后修改日期'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
