# Generated by Django 4.2.4 on 2023-10-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0016_orders_rate1_orders_rate2'),
    ]

    operations = [
        migrations.AddField(
            model_name='bindingorder',
            name='brand_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='brand_bind',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='class_bind',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='code_bind',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_1',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_2',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_3',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_4',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_5',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_6',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_7',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_8',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_9',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bindingorder',
            name='midium_bind',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]