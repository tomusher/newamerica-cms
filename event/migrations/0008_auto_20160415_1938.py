# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20160408_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='soundcloud_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
