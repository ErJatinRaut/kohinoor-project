# Generated by Django 4.1.5 on 2023-08-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=200, null=True)),
                ('standard', models.CharField(blank=True, max_length=200, null=True)),
                ('medium', models.CharField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('form1', models.IntegerField(blank=True, null=True)),
                ('form2', models.IntegerField(blank=True, null=True)),
                ('form3', models.IntegerField(blank=True, null=True)),
                ('form4', models.IntegerField(blank=True, null=True)),
                ('form5', models.IntegerField(blank=True, null=True)),
                ('form6', models.IntegerField(blank=True, null=True)),
                ('form7', models.IntegerField(blank=True, null=True)),
                ('form8', models.IntegerField(blank=True, null=True)),
                ('form9', models.IntegerField(blank=True, null=True)),
                ('form10', models.IntegerField(blank=True, null=True)),
                ('form11', models.IntegerField(blank=True, null=True)),
                ('form12', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]