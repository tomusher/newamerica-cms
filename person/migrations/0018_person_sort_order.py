# Generated by Django 3.2.18 on 2023-07-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0017_add_alt_text_to_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sort_order',
            field=models.PositiveIntegerField(help_text='Used for ordering this person on the Our People page. People with a lower sort order will appear first.', null=True, blank=True),
        ),
    ]
