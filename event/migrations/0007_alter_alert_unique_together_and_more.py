# Generated by Django 4.1.4 on 2023-03-07 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_owner'),
        ('event', '0006_alter_notification_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='alert',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='AlertMonitorTransactionMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.alert')),
                ('monitor_transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.monitortransaction')),
            ],
            options={
                'unique_together': {('account', 'alert', 'monitor_transaction')},
            },
        ),
        migrations.RemoveField(
            model_name='alert',
            name='monitor_transaction',
        ),
        migrations.AddField(
            model_name='monitortransaction',
            name='alert',
            field=models.ManyToManyField(related_name='alerts', through='event.AlertMonitorTransactionMapping', to='event.alert'),
        ),
    ]
