# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-29 19:17
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mturk', '0004_auto_20160629_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mturkhittype',
            name='keywords',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), default=[], null=True, size=None),
        ),
    ]
