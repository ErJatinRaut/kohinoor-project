# Generated by Django 5.0 on 2024-02-06 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_app', '0014_sale_bill_percent_1_sale_bill_percent_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale_bill',
            name='category1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category10',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='category9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='vend_category',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
