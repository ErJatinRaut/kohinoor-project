# Generated by Django 4.1.2 on 2023-07-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0002_orders_print_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='gather_approved',
            field=models.BooleanField(default=False),
        ),
    ]