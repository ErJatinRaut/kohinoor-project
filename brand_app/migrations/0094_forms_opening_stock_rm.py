# Generated by Django 4.2.4 on 2023-12-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0093_transaction_operation_particular1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='opening_stock_rm',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]