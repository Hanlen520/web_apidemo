# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-28 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0011_tasklist_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='elapsed_time',
            field=models.TextField(blank=True, null=True),
        ),
    ]
