# Generated by Django 4.2 on 2023-06-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0029_forms_gross'),
    ]

    operations = [
        migrations.CreateModel(
            name='material_centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre_name', models.CharField(default='', max_length=200, null=True)),
                ('stock_of_book_paper', models.CharField(default='', max_length=200, null=True)),
                ('stock_of_cover_paper', models.DateTimeField(null='True')),
                ('topi', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
