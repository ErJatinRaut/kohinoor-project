# Generated by Django 4.2.4 on 2023-12-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0092_product_by_punit22_product_by_punit33'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_operation',
            name='Particular1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaction_operation',
            name='Particular2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='transaction_operation',
            name='Particular3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
