# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-19 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magic', '0007_auto_20170929_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
                ('name', models.CharField(max_length=100)),
                ('card_sets', models.ManyToManyField(related_name='formats', to='magic.CardSet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
