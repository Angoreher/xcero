# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0001_squashed_0011_auto_20170929_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='power',
            field=models.FloatField(blank=True, null=True, verbose_name='power'),
        ),
        migrations.AlterField(
            model_name='card',
            name='toughness',
            field=models.FloatField(blank=True, null=True, verbose_name='toughness'),
        ),
    ]
