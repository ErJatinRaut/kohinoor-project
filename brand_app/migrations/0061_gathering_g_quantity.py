# Generated by Django 4.2.4 on 2023-09-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0060_printing_transfer1_printing_transfer10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='g_quantity',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
