# Generated by Django 4.1.5 on 2023-01-30 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0008_books_subject_classes_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_forms', models.CharField(default='', max_length=200, null=True)),
                ('form_length', models.CharField(default='', max_length=200, null=True)),
                ('form_width', models.CharField(default='', max_length=200, null=True)),
                ('form_gsm', models.CharField(default='', max_length=200, null=True)),
                ('no_of_pages', models.CharField(default='', max_length=200, null=True)),
                ('forms_added_on', models.DateTimeField(null='True')),
            ],
        ),
    ]
