# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-13 18:05
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('in_depth', '0009_auto_20170203_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indepthsection',
            name='panels',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('panel_title', wagtail.blocks.CharBlock(required=True)), ('panel_color_theme', wagtail.blocks.ChoiceBlock(choices=[(b'white', b'White'), (b'grey', b'Grey'), (b'black', b'Black')])), ('panel_body', wagtail.blocks.StreamBlock([(b'introduction', wagtail.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.blocks.RichTextBlock()), (b'inline_image', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial'))], icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.blocks.StructBlock([(b'button_text', wagtail.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.blocks.StructBlock([(b'source_url', wagtail.blocks.URLBlock(required=True)), (b'width', wagtail.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=False)), (b'subheading', wagtail.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.blocks.CharBlock(required=True))], icon=b'code')), (b'google_map', wagtail.blocks.StructBlock([(b'use_page_address', wagtail.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.blocks.TextBlock(required=False)), (b'city', wagtail.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.blocks.TextBlock(default=b'200', required=False))], icon=b'site')), (b'schedule', wagtail.blocks.StreamBlock([(b'days', wagtail.blocks.StructBlock([(b'collapsible', wagtail.blocks.BooleanBlock(default=True, help_text=b'Allow schedule sessions to expand and collapse', required=False)), (b'day', wagtail.blocks.ChoiceBlock(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')], default=1, help_text=b'What day of the conference is this session on?', required=False)), (b'start_time', wagtail.blocks.TimeBlock(required=False)), (b'end_time', wagtail.blocks.TimeBlock(required=False)), (b'sessions', wagtail.blocks.StreamBlock([(b'session', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.TextBlock()), (b'session_type', wagtail.blocks.ChoiceBlock(choices=[(b'panel', b'Panel'), (b'lecture', b'Lecture'), (b'break', b'Break'), (b'meal', b'Meal'), (b'reception', b'Reception'), (b'registration', b'Registration')])), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'start_time', wagtail.blocks.TimeBlock(required=False)), (b'end_time', wagtail.blocks.TimeBlock(required=False)), (b'speakers', wagtail.blocks.StreamBlock([(b'speaker', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.TextBlock(required=True)), (b'title', wagtail.blocks.TextBlock(required=False))]))])), (b'archived_video_link', wagtail.blocks.URLBlock(help_text=b'Enter youtube link after conference', required=False))]))]))]))], help_text=b'1 to 2 day schedule of events', icon=b'date')), (b'people', wagtail.blocks.StreamBlock([(b'person', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.TextBlock(required=True)), (b'title', wagtail.blocks.TextBlock(help_text=b'125 character limit', max_length=125, required=False)), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'twitter', wagtail.blocks.URLBlock(required=False))]))], help_text=b'Grid of people with short bios that appear on click', icon=b'group')), (b'panels', wagtail.blocks.StreamBlock([(b'panel', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.TextBlock()), (b'body', wagtail.blocks.StreamBlock([(b'introduction', wagtail.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.blocks.RichTextBlock()), (b'inline_image', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial'))], icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.blocks.StructBlock([(b'button_text', wagtail.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.blocks.StructBlock([(b'source_url', wagtail.blocks.URLBlock(required=True)), (b'width', wagtail.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=False)), (b'subheading', wagtail.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.blocks.CharBlock(required=True))], icon=b'code')), (b'google_map', wagtail.blocks.StructBlock([(b'use_page_address', wagtail.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.blocks.TextBlock(required=False)), (b'city', wagtail.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.blocks.TextBlock(default=b'200', required=False))], icon=b'site'))]))], icon=b'doc-empty-inverse'))], icon=b'list-ul')), (b'image', wagtail.images.blocks.ImageChooserBlock(help_text=b'Legacy option. Consider using Inline Image instead.', icon=b'placeholder', template=b'blocks/image_block.html')), (b'collapsible', wagtail.blocks.StructBlock([(b'hidden_by_default', wagtail.blocks.StreamBlock([(b'introduction', wagtail.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.blocks.RichTextBlock()), (b'inline_image', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial'))], icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.blocks.StructBlock([(b'button_text', wagtail.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.blocks.StructBlock([(b'source_url', wagtail.blocks.URLBlock(required=True)), (b'width', wagtail.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=False)), (b'subheading', wagtail.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.blocks.CharBlock(required=True))], icon=b'code')), (b'google_map', wagtail.blocks.StructBlock([(b'use_page_address', wagtail.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.blocks.TextBlock(required=False)), (b'city', wagtail.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.blocks.TextBlock(default=b'200', required=False))], icon=b'site')), (b'schedule', wagtail.blocks.StreamBlock([(b'days', wagtail.blocks.StructBlock([(b'collapsible', wagtail.blocks.BooleanBlock(default=True, help_text=b'Allow schedule sessions to expand and collapse', required=False)), (b'day', wagtail.blocks.ChoiceBlock(choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')], default=1, help_text=b'What day of the conference is this session on?', required=False)), (b'start_time', wagtail.blocks.TimeBlock(required=False)), (b'end_time', wagtail.blocks.TimeBlock(required=False)), (b'sessions', wagtail.blocks.StreamBlock([(b'session', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.TextBlock()), (b'session_type', wagtail.blocks.ChoiceBlock(choices=[(b'panel', b'Panel'), (b'lecture', b'Lecture'), (b'break', b'Break'), (b'meal', b'Meal'), (b'reception', b'Reception'), (b'registration', b'Registration')])), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'start_time', wagtail.blocks.TimeBlock(required=False)), (b'end_time', wagtail.blocks.TimeBlock(required=False)), (b'speakers', wagtail.blocks.StreamBlock([(b'speaker', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.TextBlock(required=True)), (b'title', wagtail.blocks.TextBlock(required=False))]))])), (b'archived_video_link', wagtail.blocks.URLBlock(help_text=b'Enter youtube link after conference', required=False))]))]))]))], help_text=b'1 to 2 day schedule of events', icon=b'date')), (b'people', wagtail.blocks.StreamBlock([(b'person', wagtail.blocks.StructBlock([(b'name', wagtail.blocks.TextBlock(required=True)), (b'title', wagtail.blocks.TextBlock(help_text=b'125 character limit', max_length=125, required=False)), (b'description', wagtail.blocks.RichTextBlock(required=False)), (b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=False)), (b'twitter', wagtail.blocks.URLBlock(required=False))]))], help_text=b'Grid of people with short bios that appear on click', icon=b'group')), (b'panels', wagtail.blocks.StreamBlock([(b'panel', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.TextBlock()), (b'body', wagtail.blocks.StreamBlock([(b'introduction', wagtail.blocks.RichTextBlock(icon=b'openquote')), (b'heading', wagtail.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.blocks.RichTextBlock()), (b'inline_image', wagtail.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock(icon=b'image', required=True)), (b'align', wagtail.blocks.ChoiceBlock(choices=[(b'left', b'Left'), (b'right', b'Right'), (b'full-width', b'Full Width')])), (b'width', wagtail.blocks.ChoiceBlock(choices=[(b'initial', b'Auto'), (b'60%', b'60%'), (b'50%', b'50%'), (b'33.333%', b'33%'), (b'25%', b'25%')], default=b'initial'))], icon=b'image')), (b'video', wagtail.embeds.blocks.EmbedBlock(icon=b'media')), (b'table', wagtail.contrib.table_block.blocks.TableBlock()), (b'button', wagtail.blocks.StructBlock([(b'button_text', wagtail.blocks.CharBlock(max_length=50, required=True)), (b'button_link', wagtail.blocks.URLBlock(default=b'https://www.', required=True)), (b'alignment', wagtail.blocks.ChoiceBlock(choices=[(b'left-aligned', b'Left'), (b'center-aligned', b'Center')]))])), (b'iframe', wagtail.blocks.StructBlock([(b'source_url', wagtail.blocks.URLBlock(required=True)), (b'width', wagtail.blocks.IntegerBlock(help_text=b'The maximum possible iframe width is 1050', max_value=1050)), (b'height', wagtail.blocks.IntegerBlock())], icon=b'link')), (b'dataviz', wagtail.blocks.StructBlock([(b'title', wagtail.blocks.CharBlock(required=False)), (b'subheading', wagtail.blocks.RichTextBlock(required=False)), (b'max_width', wagtail.blocks.IntegerBlock()), (b'show_chart_buttons', wagtail.blocks.BooleanBlock(default=False, required=False)), (b'container_id', wagtail.blocks.CharBlock(required=True))], icon=b'code')), (b'google_map', wagtail.blocks.StructBlock([(b'use_page_address', wagtail.blocks.BooleanBlock(default=False, help_text=b'If selected, map will use the address already defined for this page, if applicable. For most posts besides events, this should be left unchecked and the form below should be completed.', required=False)), (b'street', wagtail.blocks.TextBlock(required=False)), (b'city', wagtail.blocks.TextBlock(default=b'Washington', required=False)), (b'state', wagtail.blocks.TextBlock(default=b'D.C.', required=False)), (b'zipcode', wagtail.blocks.TextBlock(default=b'200', required=False))], icon=b'site'))]))], icon=b'doc-empty-inverse'))], icon=b'list-ul')), (b'image', wagtail.images.blocks.ImageChooserBlock(help_text=b'Legacy option. Consider using Inline Image instead.', icon=b'placeholder', template=b'blocks/image_block.html'))]))]))]))]))], blank=True, null=True),
        ),
    ]
