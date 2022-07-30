# Generated by Django 3.0 on 2022-06-09 13:48

from django.db import migrations


def forwards_func(apps, schema_editor):
    oc_lettings_address = apps.get_model("oc_lettings_site", "Address")
    oc_lettings_letting = apps.get_model("oc_lettings_site", "Letting")
    oc_lettings_profile = apps.get_model("oc_lettings_site", "Profile")

    Address = apps.get_model("lettings", "Address")
    Letting = apps.get_model("lettings", "Letting")
    Profile = apps.get_model("profiles", "Profile")

    db_alias = schema_editor.connection.alias
    addresses = []
    for line in oc_lettings_address.objects.all().order_by("id"):
        addresses.append(
            Address(
                id=line.id,
                number=line.number,
                street=line.street,
                city=line.city,
                state=line.state,
                zip_code=line.zip_code,
                country_iso_code=line.country_iso_code,
            )
        )
    Address.objects.using(db_alias).bulk_create(addresses)

    lettings = []
    for line in oc_lettings_letting.objects.all().order_by("id"):
        lettings.append(
            Letting(
                id=line.id,
                title=line.title,
                address=Address.objects.get(id=line.address.id),
            )
        )
    Letting.objects.using(db_alias).bulk_create(lettings)

    profiles = []
    for line in oc_lettings_profile.objects.all().order_by("id"):
        profiles.append(
            Profile(
                id=line.id,
                user=line.user,
                favorite_city=line.favorite_city,
            )
        )
    Profile.objects.using(db_alias).bulk_create(profiles)


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0001_initial"),
        ("lettings", "0001_initial"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
