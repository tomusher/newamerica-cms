# Generated by Django 3.2.18 on 2023-04-21 21:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0018_auto_20210730_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='sidebar_menu_about_us_pages',
            field=wagtail.fields.StreamField([('Item', wagtail.blocks.PageChooserBlock())], blank=True, null=True, use_json_field=True),
        ),
    ]
