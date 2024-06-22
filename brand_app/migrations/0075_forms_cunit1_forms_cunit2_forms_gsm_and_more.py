# Generated by Django 4.2.4 on 2023-10-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0074_forms_gsm_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='cunit1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='cunit2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='gsm',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='opening_stock_value',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='p_length',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='p_width',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='print_name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='qunit',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='qunit1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='qunit2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='qunit3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='rmalias',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='rmname',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='unit1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='unit1_conversion',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='unit2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='unit2_conversion',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='forms',
            name='unit3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
