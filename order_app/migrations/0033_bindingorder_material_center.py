# Generated by Django 5.0 on 2024-02-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0032_alter_bom_bom_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='bindingorder',
            name='material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]