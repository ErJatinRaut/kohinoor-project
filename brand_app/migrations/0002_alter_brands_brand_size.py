# Generated by Django 4.1.5 on 2023-01-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='brand_size',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
