# Generated by Django 4.2.4 on 2023-08-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0040_alter_distributors_distributor_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='printing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_vender_name', models.CharField(default='', max_length=200, null=True)),
                ('p_vender_address', models.CharField(default='', max_length=200, null=True)),
                ('p_vender_email', models.CharField(default='', max_length=200, null=True)),
                ('p_vender_mob', models.CharField(default='', max_length=200, null=True)),
                ('p_brand_name_1', models.CharField(default='', max_length=200, null=True)),
                ('p_class_name_1', models.CharField(default='', max_length=200, null=True)),
                ('p_medium_1', models.CharField(default='', max_length=200, null=True)),
                ('p_subject_1', models.CharField(default='', max_length=200, null=True)),
                ('p_quantity_1', models.CharField(default='', max_length=200, null=True)),
                ('p_rim_1', models.CharField(default='', max_length=200, null=True)),
                ('p_pages_1', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_1', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_1', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_2', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_3', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_4', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_2', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_3', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_4', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_5', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_6', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_7', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_5', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_6', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_7', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_8', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_9', models.CharField(default='', max_length=200, null=True)),
                ('p_printing_received_form_10', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_8', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_9', models.CharField(default='', max_length=200, null=True)),
                ('p_print_wastage_form_10', models.CharField(default='', max_length=200, null=True)),
                ('p_single_1', models.CharField(default='', max_length=200, null=True)),
                ('p_double_1', models.CharField(default='', max_length=200, null=True)),
                ('p_four_1', models.CharField(default='', max_length=200, null=True)),
                ('p_print_date', models.CharField(default='', max_length=200)),
                ('total_received_forms', models.CharField(default='', max_length=200, null=True)),
                ('total_wastage_forms', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
