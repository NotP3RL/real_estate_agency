# Generated by Django 2.2.24 on 2022-12-28 10:48

from django.db import migrations


def move_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all().iterator():
        flats = Flat.objects.filter(owner=owner.name, owners_phonenumber=owner.phonenumber)
        owner.flats.set(flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20221228_1807'),
    ]

    operations = [
        migrations.RunPython(move_flats)
    ]
