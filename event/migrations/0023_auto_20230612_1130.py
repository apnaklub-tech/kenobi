# Generated by Django 4.1.4 on 2023-06-12 11:30
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0022_alter_event_event_source_and_more'),
    ]

    operations = [
        TrigramExtension(),
    ]
