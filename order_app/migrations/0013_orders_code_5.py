# Generated by Django 4.2.4 on 2023-09-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0012_orders_code_4'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='code_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
