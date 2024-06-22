# Generated by Django 4.2.4 on 2023-12-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0100_vouchers_account_vouchers_account1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='conversion_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_unit', models.CharField(default='', max_length=200, null=True)),
                ('sub_unit', models.CharField(default='', max_length=200, null=True)),
                ('Con_factor', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='master_unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name_master', models.CharField(default='', max_length=200, null=True)),
                ('unit_Alias', models.CharField(default='', max_length=200, null=True)),
                ('unit_print_name', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]