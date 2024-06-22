# Generated by Django 4.1.5 on 2023-01-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0004_alter_brands_brand_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(default='', max_length=200, null=True)),
                ('class_book', models.CharField(default='', max_length=200, null=True)),
                ('classes_added_on', models.DateTimeField(null='True')),
            ],
        ),
    ]
