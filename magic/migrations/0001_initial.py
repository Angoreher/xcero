# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='code')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('gatherer_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='gatherer code')),
                ('old_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='old_code')),
                ('magic_cards_info_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='magic cards info code')),
                ('release_date', models.CharField(blank=True, max_length=255, null=True, verbose_name='release date')),
                ('border', models.CharField(blank=True, max_length=255, null=True, verbose_name='barder')),
                ('set_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='type')),
                ('block', models.CharField(blank=True, max_length=255, null=True, verbose_name='block')),
                ('online_only', models.CharField(blank=True, max_length=255, null=True, verbose_name='online only')),
                ('booster', models.CharField(blank=True, max_length=255, null=True, verbose_name='booster')),
                ('mkm_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='mkm_id')),
                ('mkm_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='mkm_name')),
                ('last_updated_at', models.DateTimeField(blank=True, null=True, verbose_name='last updated at')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
