# Generated by Django 4.2.5 on 2023-09-30 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place2',
            old_name='image',
            new_name='img',
        ),
    ]