# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20170929_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(max_length=1000),
        ),
    ]