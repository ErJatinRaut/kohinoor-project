# Generated by Django 4.2 on 2023-05-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0025_books_cover_books_form1_books_form10_books_form11_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='forms',
            name='per_kg_weight',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
