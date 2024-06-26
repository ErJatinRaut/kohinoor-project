# Generated by Django 4.1.5 on 2023-01-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0013_books_book_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='venders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(default='', max_length=200, null=True)),
                ('vender_contact', models.CharField(default='', max_length=200, null=True)),
                ('vender_email', models.CharField(default='', max_length=200, null=True)),
                ('vender_gstin_no', models.CharField(default='', max_length=200, null=True)),
                ('vender_address', models.CharField(default='', max_length=200, null=True)),
                ('vender_created_by', models.DateTimeField(null='True')),
            ],
        ),
    ]
