# Generated by Django 5.0 on 2024-01-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0107_item_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='subbrand',
            name='binding_form_size',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subbrand',
            name='printing_form_size',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]