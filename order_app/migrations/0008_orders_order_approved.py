# Generated by Django 4.1.5 on 2023-08-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0007_remove_orders_complete_book_gathered_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_approved',
            field=models.BooleanField(default=False),
        ),
    ]
