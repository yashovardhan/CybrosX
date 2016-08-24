# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0106_auto_20160623_0421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paypalpayoutlog',
            old_name='created_timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='paypalpayoutlog',
            old_name='last_updated',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender_type',
            field=models.SmallIntegerField(choices=[(1, b'self'), (2, b'project_owner'), (3, b'system')], default=1),
        ),
    ]
