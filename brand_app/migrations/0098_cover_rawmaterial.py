# Generated by Django 4.2.4 on 2023-12-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0097_forms_waste_forms_waste_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover_rawmaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmname', models.CharField(default='', max_length=200, null=True)),
                ('cmalias', models.CharField(default='', max_length=200, null=True)),
                ('cprint_name', models.CharField(default='', max_length=200, null=True)),
                ('cqunit', models.CharField(default='', max_length=200, null=True)),
                ('copening_stock_value', models.CharField(default='', max_length=200, null=True)),
                ('cgsm', models.CharField(default='', max_length=200, null=True)),
                ('cp_width', models.CharField(default='', max_length=200, null=True)),
                ('cp_length', models.CharField(default='', max_length=200, null=True)),
                ('cunit1', models.CharField(default='', max_length=200, null=True)),
                ('cqunit1', models.CharField(default='', max_length=200, null=True)),
                ('cunit2', models.CharField(default='', max_length=200, null=True)),
                ('cqunit2', models.CharField(default='', max_length=200, null=True)),
                ('cunit3', models.CharField(default='', max_length=200, null=True)),
                ('cqunit3', models.CharField(default='', max_length=200, null=True)),
                ('cunit1_conversion', models.CharField(default='', max_length=200, null=True)),
                ('cmunit1', models.CharField(default='', max_length=200, null=True)),
                ('cunit2_conversion', models.CharField(default='', max_length=200, null=True)),
                ('cmunit2', models.CharField(default='', max_length=200, null=True)),
                ('opening_stock_rm', models.CharField(default='', max_length=200, null=True)),
                ('gross', models.CharField(default='', max_length=200, null=True)),
                ('p_date', models.CharField(default='', max_length=200, null=True)),
                ('cwaste_percent', models.CharField(default='', max_length=200, null=True)),
                ('cWaste', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]