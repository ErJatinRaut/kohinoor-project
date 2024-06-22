# Generated by Django 4.1.5 on 2023-01-31 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0009_forms'),
    ]

    operations = [
        migrations.CreateModel(
            name='mediums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(default='', max_length=200, null=True)),
                ('medium_added_on', models.DateTimeField(null='True')),
            ],
        ),
        migrations.RemoveField(
            model_name='classes',
            name='medium',
        ),
    ]
