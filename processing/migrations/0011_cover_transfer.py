# Generated by Django 5.0 on 2024-02-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0010_transfer_printing_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='cover_transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('vender_transfer_to', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('vender_transfer_from', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_voucher_no', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_subject1', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_qty1', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_unit1', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_subject2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_qty2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_unit2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_subject3', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_qty3', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_unit3', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_subject4', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_qty4', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_unit4', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_subject5', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_qty5', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('cover_transfer_unit5', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]
