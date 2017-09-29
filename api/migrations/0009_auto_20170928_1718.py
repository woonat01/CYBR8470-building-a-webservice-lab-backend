# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170927_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='exerciseneeds',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3),
        ),
        migrations.AlterField(
            model_name='breed',
            name='friendliness',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3),
        ),
        migrations.AlterField(
            model_name='breed',
            name='sheddingamount',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3),
        ),
        migrations.AlterField(
            model_name='breed',
            name='trainability',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=3),
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Breed'),
        ),
    ]
