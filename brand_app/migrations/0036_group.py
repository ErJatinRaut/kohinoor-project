# Generated by Django 4.1.2 on 2023-07-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0035_books_fourc_rate_books_onec_rate_books_twoc_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
