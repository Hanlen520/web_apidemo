# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-21 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0002_remove_interface_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppPage',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('page_id', models.IntegerField(null=True)),
                ('page_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 't_app_page',
            },
        ),
        migrations.RemoveField(
            model_name='app',
            name='page_id',
        ),
        migrations.RemoveField(
            model_name='app',
            name='page_name',
        ),
        migrations.AlterField(
            model_name='interface',
            name='app_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appapi.App'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='page_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appapi.AppPage'),
        ),
        migrations.AddField(
            model_name='apppage',
            name='app_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appapi.App'),
        ),
    ]