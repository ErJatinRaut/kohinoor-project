# Generated by Django 5.0 on 2024-01-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_app', '0013_sale_bill_amount_1_sale_bill_amount_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale_bill',
            name='percent_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='percent_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='percent_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='percent_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='percent_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]