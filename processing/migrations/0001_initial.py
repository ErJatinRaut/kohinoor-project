# Generated by Django 4.1.3 on 2023-02-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gathering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_received_form', models.CharField(default='', max_length=200, null=True)),
                ('printed_form', models.CharField(default='', max_length=200, null=True)),
                ('wastage_form', models.CharField(default='', max_length=200, null=True)),
                ('gathering_added_on', models.DateTimeField(null='True')),
            ],
        ),
    ]
