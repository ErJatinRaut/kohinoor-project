# Generated by Django 4.2.4 on 2023-11-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0082_cover_scrap_voucher_other_vouchers'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_master', models.CharField(default='', max_length=200, null=True)),
                ('tehsil_master', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
