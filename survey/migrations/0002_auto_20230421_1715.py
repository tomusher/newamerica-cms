# Generated by Django 3.2.18 on 2023-04-21 21:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyshomepage',
            name='submissions',
            field=wagtail.fields.StreamField([('cta_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50, required=False)), ('description', wagtail.blocks.TextBlock(max_length=200, required=False)), ('link_text', wagtail.blocks.CharBlock(max_length=200, required=False)), ('link_url', wagtail.blocks.CharBlock(max_length=200, required=False))]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='surveyshomepage',
            name='subscribe',
            field=wagtail.fields.StreamField([('cta_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50, required=False)), ('description', wagtail.blocks.TextBlock(max_length=200, required=False)), ('link_text', wagtail.blocks.CharBlock(max_length=200, required=False)), ('link_url', wagtail.blocks.CharBlock(max_length=200, required=False))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
