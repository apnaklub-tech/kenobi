# Generated by Django 4.1.4 on 2023-03-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_monitor_is_active_alter_notification_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
