# Generated by Django 4.2.4 on 2023-10-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0064_vouchers_voucher_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuttting',
            name='complete_book',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
