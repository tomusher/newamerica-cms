# Generated by Django 3.2.18 on 2023-05-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0015_auto_20230421_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='about_image_alt',
            field=models.TextField(blank=True, default='', help_text='A concise description of the image for users of assistive technology.', verbose_name='About image alternative text'),
        ),
        migrations.AddField(
            model_name='conference',
            name='alternate_logo_alt',
            field=models.TextField(blank=True, default='', help_text='A concise description of the image for users of assistive technology.', verbose_name='Alternate logo alternative text'),
        ),
        migrations.AddField(
            model_name='conference',
            name='story_image_alt',
            field=models.TextField(blank=True, default='', help_text='A concise description of the image for users of assistive technology.', verbose_name='Cover image alternative text'),
        ),
    ]
