# Generated by Django 2.2.24 on 2022-12-14 10:45

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20221214_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='normalized_owners_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
