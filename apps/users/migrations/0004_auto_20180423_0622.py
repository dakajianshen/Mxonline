# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-23 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180407_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=10),
        ),
    ]