# Generated by Django 2.2.24 on 2022-04-19 14:43

from django.db import migrations


def add_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for owner in Owner.objects.all():
        owner.flats.set(Flat.objects.filter(owner=owner.owner))
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220419_2205'),
    ]

    operations = [
        migrations.RunPython(add_flats)
    ]
