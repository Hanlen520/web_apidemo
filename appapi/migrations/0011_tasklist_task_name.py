# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-28 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0010_auto_20170728_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='task_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
