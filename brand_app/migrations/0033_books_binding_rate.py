# Generated by Django 4.2 on 2023-06-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0032_material_centre_alias_material_centre_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='binding_rate',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]