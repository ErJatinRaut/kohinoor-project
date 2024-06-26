# Generated by Django 5.0 on 2024-02-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0130_cover_order_lamination_sheet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover_order',
            name='amount_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='bill_sundries_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='bill_sundries_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='bill_sundries_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='bill_sundries_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='bill_sundries_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='narration_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='narration_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='narration_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='narration_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='narration_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='percent_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='percent_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='percent_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='percent_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='percent_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
