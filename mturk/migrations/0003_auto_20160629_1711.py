# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-29 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mturk', '0002_auto_20160629_1710'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Qualification',
            new_name='MTurkQualification',
        ),
    ]
