# Generated by Django 5.0 on 2024-02-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0125_alter_subbrand_additionaldiscount_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover_order',
            name='material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]