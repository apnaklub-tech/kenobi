# Generated by Django 4.1.4 on 2023-04-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_alter_event_event_source_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitortransaction',
            name='event_timestamp',
        ),
        migrations.AddField(
            model_name='monitortransactioneventmapping',
            name='event_timestamp',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
