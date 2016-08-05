# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-03 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0124_auto_20160725_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoomerangLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('min_rating', models.FloatField(default=3.0)),
                ('rating_updated_at', models.DateTimeField(null=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boomerang_logs', to='crowdsourcing.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
