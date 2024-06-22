# Generated by Django 4.2.4 on 2023-12-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0090_form_printing'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover_order',
            name='amount1',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount10',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount2',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount3',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount4',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount5',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount6',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount7',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount8',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='amount9',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order10',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='plate_order9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order1',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order10',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order2',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order3',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order4',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order5',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order6',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order7',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order8',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='quantity_order9',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order1',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order10',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order2',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order3',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order4',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order5',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order6',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order7',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order8',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cover_order',
            name='rate_order9',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
