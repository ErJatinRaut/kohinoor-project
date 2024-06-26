# Generated by Django 4.2.4 on 2023-11-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0020_bindingorder_b_amount_bindingorder_b_amount1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_sundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bil_sundries_name', models.CharField(default='', max_length=200, null=True)),
                ('bill_sundries_alias', models.CharField(default='', max_length=200, null=True)),
                ('bill_sundry_type', models.CharField(default='', max_length=200, null=True)),
                ('bill_sundry_nature', models.CharField(default='', max_length=200, null=True)),
                ('bill_sundry_default_value', models.CharField(default='', max_length=200, null=True)),
                ('bill_sundry_total', models.CharField(default='', max_length=200, null=True)),
                ('cost_good_sale', models.CharField(default='', max_length=200, null=True)),
                ('cost_good_purchase', models.CharField(default='', max_length=200, null=True)),
                ('cost_good_material_receipt', models.CharField(default='', max_length=200, null=True)),
                ('cost_good_stock_transfer', models.CharField(default='', max_length=200, null=True)),
                ('acc_affect_accounting', models.CharField(default='', max_length=200, null=True)),
                ('sale_amount_accounting', models.CharField(default='', max_length=200, null=True)),
                ('specify_acc', models.CharField(default='', max_length=200, null=True)),
                ('account_head_post', models.CharField(default='', max_length=200, null=True)),
                ('account_tax', models.CharField(default='', max_length=200, null=True)),
                ('adjust_party_amount', models.CharField(default='', max_length=200, null=True)),
                ('post_over_and_above', models.CharField(default='', max_length=200, null=True)),
                ('purchase_affect', models.CharField(default='', max_length=200, null=True)),
                ('purchase_amount', models.CharField(default='', max_length=200, null=True)),
                ('purchase_account_head', models.CharField(default='', max_length=200, null=True)),
                ('purchase_party_amount', models.CharField(default='', max_length=200, null=True)),
                ('zero_tax_item', models.CharField(default='', max_length=200, null=True)),
                ('stock_affects_accounting', models.CharField(default='', max_length=200, null=True)),
                ('stock_other_side', models.CharField(default='', max_length=200, null=True)),
                ('stock_account_head_to_post', models.CharField(default='', max_length=200, null=True)),
                ('stock_adjust_party', models.CharField(default='', max_length=200, null=True)),
                ('stock_specify_acc_here', models.CharField(default='', max_length=200, null=True)),
                ('stock_post_over_above', models.CharField(default='', max_length=200, null=True)),
                ('percent', models.CharField(default='', max_length=200, null=True)),
                ('selective_calculation', models.CharField(default='', max_length=200, null=True)),
                ('item_basic_amt', models.CharField(default='', max_length=200, null=True)),
                ('consolidate_bill_sundry', models.CharField(default='', max_length=200, null=True)),
                ('bill_sundry_amount', models.CharField(default='', max_length=200, null=True)),
                ('round_off_bill', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
