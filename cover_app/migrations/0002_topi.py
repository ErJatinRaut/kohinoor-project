# Generated by Django 4.2.4 on 2023-11-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_no_of_ups', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject1', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject2', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject3', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject4', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject5', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject6', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject7', models.CharField(default='', max_length=200, null=True)),
                ('t_subject8', models.CharField(default='', max_length=200, null=True)),
                ('t_subject9', models.CharField(default='', max_length=200, null=True)),
                ('t_subject10', models.CharField(default='', max_length=200, null=True)),
                ('t_subject11', models.CharField(default='', max_length=200, null=True)),
                ('t_subject12', models.CharField(default='', max_length=200, null=True)),
                ('t_subject13', models.CharField(default='', max_length=200, null=True)),
                ('t_subject14', models.CharField(default='', max_length=200, null=True)),
                ('t_subject15', models.CharField(default='', max_length=200, null=True)),
                ('t_subject16', models.CharField(default='', max_length=200, null=True)),
                ('t_subject17', models.CharField(default='', max_length=200, null=True)),
                ('t_subject18', models.CharField(default='', max_length=200, null=True)),
                ('t_subject19', models.CharField(default='', max_length=200, null=True)),
                ('t_subject20', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject21', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject22', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject23', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject24', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject25', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject26', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('t_subject27', models.CharField(default='', max_length=200, null=True)),
                ('t_subject28', models.CharField(default='', max_length=200, null=True)),
                ('t_subject29', models.CharField(default='', max_length=200, null=True)),
                ('t_subject30', models.CharField(default='', max_length=200, null=True)),
                ('t_subject31', models.CharField(default='', max_length=200, null=True)),
                ('t_subject32', models.CharField(default='', max_length=200, null=True)),
                ('t_paper_to_be_used', models.CharField(default='', max_length=200, null=True)),
                ('t_quantity', models.CharField(default='', max_length=200, null=True)),
                ('t_plate_no', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
    ]
