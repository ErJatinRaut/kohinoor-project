# Generated by Django 4.1.2 on 2023-07-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0003_orders_gather_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='binding_approved',
            field=models.BooleanField(default=False),
        ),
    ]