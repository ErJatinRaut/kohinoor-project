# Generated by Django 4.2.4 on 2023-12-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0095_binder_ledger_debit_binder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cutter_ledger',
            name='cutting_rate_sheet',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
