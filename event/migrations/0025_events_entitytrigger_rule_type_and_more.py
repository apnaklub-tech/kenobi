# Generated by Django 4.1.4 on 2023-09-09 01:58

import clickhouse_backend.models
from django.db import migrations, models
import prototype.fields


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0024_events_alter_event_event_source_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="entitytrigger",
            name="rule_type",
            field=models.IntegerField(
                choices=[(0, "UNKNOWN"), (1, "LAST_EVENT"), (2, "EVENT_COUNT"), (3, "EVENT_OCCURS")],
                db_index=True,
                default=1,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="entitytrigger",
            name="type",
            field=models.IntegerField(
                choices=[
                    (0, "UNKNOWN_TYPE"),
                    (1, "PER_EVENT"),
                    (2, "AGGREGATED_EVENTS"),
                ],
                db_index=True,
            ),
        )
    ]
