# Generated by Django 4.1.5 on 2023-01-31 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0011_rename_books_cost_books_books_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='no_of_pages',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
