# Generated by Django 5.0 on 2024-01-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0117_cover_rawmaterial_cover_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='gathering',
            name='Material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
