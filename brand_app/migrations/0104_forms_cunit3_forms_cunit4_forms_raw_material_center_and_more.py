# Generated by Django 5.0 on 2023-12-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0103_subbrand_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='cunit3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='cunit4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='raw_material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='unit3_conversion',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='unit4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item_creation',
            name='item_material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product_by',
            name='by_material_center',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
