# Generated by Django 4.2.4 on 2023-09-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0045_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bindingvender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name1', models.CharField(default='', max_length=200, null=True)),
                ('vender_contact1', models.CharField(default='', max_length=200, null=True)),
                ('vender_email1', models.CharField(default='', max_length=200, null=True)),
                ('vender_gstin_no1', models.CharField(default='', max_length=200, null=True)),
                ('vender_address1', models.CharField(default='', max_length=200, null=True)),
                ('vender_created_by1', models.CharField(default='', max_length=200, null=True)),
                ('vender_group1', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
