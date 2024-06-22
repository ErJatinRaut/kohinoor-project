# Generated by Django 5.0 on 2023-12-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0024_bom_bom_item_name_bom_bom_item_name_1_bom_bom_qty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sale_voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_voucher_date', models.CharField(max_length=100)),
                ('sl_voucher_series', models.CharField(max_length=100)),
                ('sl_vehicle_no', models.CharField(max_length=100)),
                ('sl_voucher_sale_type', models.CharField(max_length=100)),
                ('sl_voucher_party', models.CharField(max_length=50)),
                ('sl_voucher_narration', models.CharField(max_length=50)),
                ('sl_voucher_item_name_1', models.CharField(blank=True, max_length=50, null=True)),
                ('sl_voucher_qty_1', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_voucher_unit_1', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_voucher_price_1', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_voucher_amount_1', models.CharField(blank=True, max_length=100, null=True)),
                ('dynamic_data', models.JSONField(blank=True, null=True)),
                ('dynamic_data1', models.JSONField(blank=True, null=True)),
                ('sl_voucher_item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sl_voucher_qty', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_voucher_unit', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_voucher_price', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_voucher_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_bill_sundries', models.CharField(blank=True, max_length=50, null=True)),
                ('sl_narration', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_zero', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_ammount', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_bill_sundries_1', models.CharField(blank=True, max_length=50, null=True)),
                ('sl_narration_1', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_zero_1', models.CharField(blank=True, max_length=100, null=True)),
                ('sl_ammount_1', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]