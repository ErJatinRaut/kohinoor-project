# Generated by Django 4.2.4 on 2023-09-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing_app', '0005_bittipacking_packing_p_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='packing',
            name='p_book_code',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='packing',
            name='p_medium',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]