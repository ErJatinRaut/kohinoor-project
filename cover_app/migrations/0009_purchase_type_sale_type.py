# Generated by Django 4.2.4 on 2023-11-25 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_app', '0008_cost_production'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, null=True)),
                ('alias', models.CharField(default='', max_length=200, null=True)),
                ('print_name', models.CharField(default='', max_length=200, null=True)),
                ('default_value', models.CharField(default='', max_length=200, null=True)),
                ('sub_total_heading', models.CharField(default='', max_length=200, null=True)),
                ('bill_sundry_nature', models.CharField(default='', max_length=200, null=True)),
                ('affected_good', models.CharField(default='', max_length=200, null=True)),
                ('adjust_amount', models.CharField(default='', max_length=200, null=True)),
                ('account_past', models.CharField(default='', max_length=200, null=True)),
                ('affected_good_purchase', models.CharField(default='', max_length=200, null=True)),
                ('adjust_purchase_account', models.CharField(default='', max_length=200, null=True)),
                ('account_heat', models.CharField(default='', max_length=200, null=True)),
                ('affected_material_issue', models.CharField(default='', max_length=200, null=True)),
                ('affected_material_receipt', models.CharField(default='', max_length=200, null=True)),
                ('affected_stock_transfer', models.CharField(default='', max_length=200, null=True)),
                ('p_specify_here', models.CharField(default='', max_length=200, null=True)),
                ('p_taxable_voucher', models.CharField(default='', max_length=200, null=True)),
                ('p_local', models.CharField(default='', max_length=200, null=True)),
                ('p_stock_transfer', models.CharField(default='', max_length=200, null=True)),
                ('p_single_tax', models.CharField(default='', max_length=200, null=True)),
                ('p_sale_date', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_sale_date', models.CharField(default='', max_length=200, null=True)),
                ('sale_type', models.CharField(default='', max_length=200, null=True)),
                ('sale_account', models.CharField(default='', max_length=200, null=True)),
                ('taxation_type', models.CharField(default='', max_length=200, null=True)),
                ('tax_invoice', models.CharField(default='', max_length=200, null=True)),
                ('specify_here', models.CharField(default='', max_length=200, null=True)),
                ('specify_voucher', models.CharField(default='', max_length=200, null=True)),
                ('taxable_voucher', models.CharField(default='', max_length=200, null=True)),
                ('t_exempt', models.CharField(default='', max_length=200, null=True)),
                ('taxable_item', models.CharField(default='', max_length=200, null=True)),
                ('reverse_charge', models.CharField(default='', max_length=200, null=True)),
                ('non_gst', models.CharField(default='', max_length=200, null=True)),
                ('zero_rated', models.CharField(default='', max_length=200, null=True)),
                ('nil_rated', models.CharField(default='', max_length=200, null=True)),
                ('local', models.CharField(default='', max_length=200, null=True)),
                ('central', models.CharField(default='', max_length=200, null=True)),
                ('stock_transfer', models.CharField(default='', max_length=200, null=True)),
                ('others', models.CharField(default='', max_length=200, null=True)),
                ('deemed_export', models.CharField(default='', max_length=200, null=True)),
                ('multi_rate', models.CharField(default='', max_length=200, null=True)),
                ('single_tax', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]