# Generated by Django 5.0 on 2024-01-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0119_binding_material_center'),
    ]

    operations = [
        migrations.AddField(
            model_name='manual',
            name='Material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
