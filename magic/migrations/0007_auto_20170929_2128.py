# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 00:28
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0006_auto_20170929_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardset',
            name='booster',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]