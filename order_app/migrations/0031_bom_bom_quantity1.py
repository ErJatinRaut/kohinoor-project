# Generated by Django 5.0 on 2024-01-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0030_orders_amount_1_orders_amount_10_orders_amount_11_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bom',
            name='bom_quantity1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
