# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-27 21:18
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20180226_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allreportshomepage',
            options={'verbose_name': 'Reports Homepage'},
        ),
        migrations.AlterField(
            model_name='report',
            name='sections',
            field=wagtail.fields.StreamField([(b'section', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.TextBlock()), (b'body', wagtail.blocks.StreamBlock([(b'introduction', wagtail.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.blocks.CharBlock(classname=b'full title', icon=b'title', template=b'blocks/heading.html')), (b'paragraph', wagtail.blocks.RichTextBlock()), (b'inline_image', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.blocks.ChoiceBlock(choices=[(b'center', b'Centered'), (b'left', b'Left'), (b'right', b'Right')], default=b'centered')), (b'width', wagtail.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'width-133', b'Medium'), (b'width-166', b'Large'), (b'width-200', b'X-Large')], default=b'initial')), (b'figure_number', wagtail.blocks.CharBlock(max_length=3, required=False)), (b'figure_title', wagtail.blocks.CharBlock(max_length=100, required=False)), (b'open_image_on_click', wagtail.blocks.BooleanBlock(default=False, required=False))], icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.blocks.StructBlock([(b'button_text', wagtail.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.blocks.StructBlock([(b'source_url', wagtail.blocks.URLBlock(required=True)), (b'width', wagtail.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=False)), (b'subheading', wagtail.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.blocks.CharBlock(required=True))], icon=b'code')), (b'timeline', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=True)), (b'subheading', wagtail.blocks.CharBlock(required=False)), (b'default_view', wagtail.blocks.ChoiceBlock(choices=[(b'timeline', b'Timeline'), (b'list', b'List')], default=b'timeline', help_text=b'Should the default view be a timeline or a list?', required=False)), (b'major_timeline_splits', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=True)), (b'start_date', wagtail.blocks.DateBlock(required=True)), (b'end_date', wagtail.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_eras', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=True)), (b'start_date', wagtail.blocks.DateBlock(required=True)), (b'end_date', wagtail.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))]), default=b'', required=False)), (b'event_categories', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(), default=b'', required=False)), (b'event_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=True)), (b'italicize_title', wagtail.blocks.BooleanBlock(default=False, required=False)), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'category', wagtail.blocks.CharBlock(required=False)), (b'start_date', wagtail.blocks.DateBlock(required=True)), (b'end_date', wagtail.blocks.DateBlock(required=False)), (b'date_display_type', wagtail.blocks.ChoiceBlock(choices=[(b'year', b'Year'), (b'month', b'Month'), (b'day', b'Day')], default=b'year', help_text=b'Controls how specific the date is displayed'))])))], icon=b'arrows-up-down')), (b'google_map', wagtail.blocks.StructBlock([(b'use_page_address', wagtail.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.blocks.TextBlock(required=False)), (b'city', wagtail.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.blocks.TextBlock(default=b'200', required=False))], icon=b'site')), (b'resource_kit', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=True)), (b'description', wagtail.blocks.TextBlock(required=False)), (b'resources', wagtail.blocks.StreamBlock([(b'post', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.CharBlock(required=True)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'resource', wagtail.blocks.PageChooserBlock(required=True))], icon=b'redirect', label=b'Post')), (b'external_resource', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.CharBlock(required=True)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'resource', wagtail.blocks.URLBlock(required=True))], icon=b'site', label=b'External resource')), (b'attachment', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.CharBlock(required=True)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'resource', wagtail.documents.blocks.DocumentChooserBlock(required=True))], icon=b'doc-full', label=b'Attachment'))]))], icon=b'folder'))]))], template=b'components/report_section_body.html'))]),
        ),
    ]
