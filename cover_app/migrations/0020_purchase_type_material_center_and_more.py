# Generated by Django 5.0 on 2024-02-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_app', '0019_topi_order_material_center'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_type',
            name='material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_return',
            name='material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]