# Generated by Django 3.2.18 on 2023-07-21 18:58

from django.db import migrations
from django.db.models import PositiveIntegerField, F
from django.db.models.functions import Cast


def convert_sort_priority(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Person = apps.get_model('person', 'Person')
    Person.objects.filter(sort_priority__isnull=False).update(
        sort_order=Cast(
            F('sort_priority'),
            output_field=PositiveIntegerField(),
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0018_person_sort_order'),
    ]

    operations = [
        migrations.RunPython(
            convert_sort_priority,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
