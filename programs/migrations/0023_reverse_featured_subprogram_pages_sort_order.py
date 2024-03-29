# Generated by Django 3.2.18 on 2024-03-29 13:46

from django.db import migrations


def reverse_featured_subprogram_pages(apps, schema_editor):
    FeaturedSubprogramPage = apps.get_model('programs', 'FeaturedSubprogramPage')
    Subprogram = apps.get_model('programs', 'Subprogram')

    for subprogram in Subprogram.objects.all():
        items_to_update = []
        if not subprogram.featured_pages.exclude(sort_order__isnull=True).exists():
            continue
        for i, featured_page in enumerate(subprogram.featured_pages.order_by('-sort_order')):
            featured_page.sort_order = i
            items_to_update.append(featured_page)
        FeaturedSubprogramPage.objects.bulk_update(
            items_to_update,
            ['sort_order'],
        )



class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0022_reverse_featured_pages_sort_order'),
    ]

    operations = [
        migrations.RunPython(reverse_featured_subprogram_pages),
    ]
