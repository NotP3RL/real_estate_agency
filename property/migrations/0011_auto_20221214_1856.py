# Generated by Django 2.2.24 on 2022-12-14 10:56

from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats:
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_number):
            flat.normalized_owners_phonenumber = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            flat.save(update_fields=['normalized_owners_phonenumber'])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_normalized_owners_phonenumber'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers)
    ]