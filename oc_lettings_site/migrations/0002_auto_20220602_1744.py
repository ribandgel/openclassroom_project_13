# Generated by Django 3.0 on 2022-06-02 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelTable(
            name='address',
            table='oc_lettings_site_address',
        ),
        migrations.AlterModelTable(
            name='letting',
            table='oc_lettings_site_letting',
        ),
        migrations.AlterModelTable(
            name='profile',
            table='oc_lettings_site_profile',
        ),
    ]
