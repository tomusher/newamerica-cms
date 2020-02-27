# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-13 21:26
from __future__ import unicode_literals

from django.db import migrations
from datetime import date

def create_ordered_date(apps, schema_editor):
    Post = apps.get_model('home', 'Post')
    for post in Post.objects.all().iterator():
        post.ordered_date_string = f'{str(post.date)}-{post.id}'
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('weekly', '0004_auto_20180424_2142'),
    ]

    operations = [
        migrations.RunPython(create_ordered_date, reverse_code=migrations.RunPython.noop),
    ]
