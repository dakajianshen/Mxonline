# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-12 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20180412_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userask',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='\u7535\u8bdd'),
        ),
    ]
