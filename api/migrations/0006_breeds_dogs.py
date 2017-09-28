# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170905_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breedname', models.CharField(max_length=1000)),
                ('size', models.CharField(max_length=1000)),
                ('friendliness', models.CharField(max_length=1000)),
                ('trainability', models.CharField(max_length=1000)),
                ('sheddingamount', models.CharField(max_length=1000)),
                ('exerciseneeds', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('age', models.CharField(max_length=1000)),
                ('gender', models.CharField(max_length=1000)),
                ('color', models.CharField(max_length=1000)),
                ('favoriteFood', models.CharField(max_length=1000)),
                ('favoriteToy', models.CharField(max_length=1000)),
                ('breed', models.CharField(max_length=1000)),
            ],
        ),
    ]