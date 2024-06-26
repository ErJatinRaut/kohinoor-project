# Generated by Django 5.0 on 2024-02-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_app', '0016_topi_t_plate_rate_topi_t_printing_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='topi_order',
            name='material_centre',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate1',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate10',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate2',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate3',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate4',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate5',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate6',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate7',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate8',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='print_rate9',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate1',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate10',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate2',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate3',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate4',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate5',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate6',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate7',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate8',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='topi_order',
            name='printing_rate9',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
