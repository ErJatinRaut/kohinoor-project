# Generated by Django 4.1.2 on 2023-07-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0039_alter_distributors_distributor_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributors',
            name='distributor_created_by',
            field=models.DateTimeField(null='True'),
        ),
    ]
