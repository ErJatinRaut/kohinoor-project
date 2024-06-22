# Generated by Django 4.2.4 on 2023-11-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_app', '0007_sale_return'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost_production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.CharField(default='', max_length=200, null=True)),
                ('closing_stock', models.CharField(default='', max_length=200, null=True)),
                ('total', models.CharField(default='', max_length=200, null=True)),
                ('opening_stock', models.CharField(default='', max_length=200, null=True)),
                ('production_date', models.CharField(default='', max_length=200, null=True)),
                ('total_production', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
