# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
