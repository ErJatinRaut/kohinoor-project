# Generated by Django 4.1.3 on 2023-02-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0015_books_per_book_forms'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='medium',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
