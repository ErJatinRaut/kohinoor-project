# Generated by Django 4.2.4 on 2023-12-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0101_conversion_unit_master_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_1',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_10',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_2',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_3',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_4',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_5',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_6',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_7',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_8',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='additionalDiscount_9',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='brand_size',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_10',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='category_9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_1',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_10',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_2',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_3',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_4',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_5',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_6',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_7',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_8',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='extraDiscount_9',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_1',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_10',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_2',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_3',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_4',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_5',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_6',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_7',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_8',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='mainDiscount_9',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='pages_per_form',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
