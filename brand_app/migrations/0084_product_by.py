# Generated by Django 4.2.4 on 2023-11-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0083_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_by',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=200, null=True)),
                ('palias', models.CharField(default='', max_length=200, null=True)),
                ('p_print_name', models.CharField(default='', max_length=200, null=True)),
                ('opening_stock_p', models.CharField(default='', max_length=200, null=True)),
                ('punit', models.CharField(default='', max_length=200, null=True)),
                ('p_opening_stock_value', models.CharField(default='', max_length=200, null=True)),
                ('p_gsm', models.CharField(default='', max_length=200, null=True)),
                ('p_p_width', models.CharField(default='', max_length=200, null=True)),
                ('p_p_length', models.CharField(default='', max_length=200, null=True)),
                ('punit1', models.CharField(default='', max_length=200, null=True)),
                ('punit2', models.CharField(default='', max_length=200, null=True)),
                ('punit3', models.CharField(default='', max_length=200, null=True)),
                ('punit1_conversion', models.CharField(default='', max_length=200, null=True)),
                ('pcunit1', models.CharField(default='', max_length=200, null=True)),
                ('punit2_conversion', models.CharField(default='', max_length=200, null=True)),
                ('pcunit2', models.CharField(default='', max_length=200, null=True)),
                ('sale_price', models.CharField(default='', max_length=200, null=True)),
                ('purchase_price', models.CharField(default='', max_length=200, null=True)),
                ('mrp', models.CharField(default='', max_length=200, null=True)),
                ('min_sale_price', models.CharField(default='', max_length=200, null=True)),
                ('sale_value_price', models.CharField(default='', max_length=200, null=True)),
                ('product_tax_local', models.CharField(default='', max_length=200, null=True)),
                ('product_tax_central', models.CharField(default='', max_length=200, null=True)),
                ('product_gst', models.CharField(default='', max_length=200, null=True)),
                ('product_item_description', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
