# Generated by Django 5.0 on 2024-02-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_app', '0023_sale_return_brand_name1_sale_return_brand_name10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name10',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='brand_name9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject10',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sale_bill',
            name='subject9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]