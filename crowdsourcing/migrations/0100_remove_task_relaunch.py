# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-16 07:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0099_task_row_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='relaunch',
        ),
    ]
