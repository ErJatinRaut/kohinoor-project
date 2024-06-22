# Generated by Django 4.2.4 on 2023-11-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0084_product_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(default='', max_length=200, null=True)),
                ('sub_brand_name', models.CharField(default='', max_length=200, null=True)),
                ('brand_subtitle', models.CharField(default='', max_length=200, null=True)),
                ('categories', models.CharField(default='', max_length=200, null=True)),
                ('main_discount', models.CharField(default='', max_length=200, null=True)),
                ('extra_discount', models.CharField(default='', max_length=200, null=True)),
                ('size', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]