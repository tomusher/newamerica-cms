# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-13 21:07
from __future__ import unicode_literals

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0004_auto_20161207_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='speakers',
            field=wagtail.fields.StreamField([(b'person', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.TextBlock(required=True)), (b'title', wagtail.blocks.TextBlock(help_text=b'125 character limit', max_length=125, required=False)), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'twitter', wagtail.blocks.URLBlock(required=False))]))], blank=True, null=True),
        ),
    ]
