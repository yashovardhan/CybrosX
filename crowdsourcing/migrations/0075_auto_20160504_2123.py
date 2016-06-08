# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0074_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='group_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='revision_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='conversationrecipient',
            name='status',
            field=models.SmallIntegerField(choices=[(1, b'Open'), (2, b'Minimized'), (3, b'Closed'), (4, b'Muted')], default=1),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('id', 'group_id')]),
        ),
    ]
