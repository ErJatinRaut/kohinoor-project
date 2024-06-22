# Generated by Django 4.1.2 on 2023-07-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0037_distributors_group_extra_discount_group_group_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distributors',
            old_name='vender_address',
            new_name='distributor_address',
        ),
        migrations.RenameField(
            model_name='distributors',
            old_name='vender_contact',
            new_name='distributor_contact',
        ),
        migrations.RenameField(
            model_name='distributors',
            old_name='vender_created_by',
            new_name='distributor_created_by',
        ),
        migrations.RenameField(
            model_name='distributors',
            old_name='vender_email',
            new_name='distributor_email',
        ),
        migrations.RenameField(
            model_name='distributors',
            old_name='vender_group',
            new_name='distributor_group',
        ),
        migrations.RenameField(
            model_name='distributors',
            old_name='vender_gstin_no',
            new_name='distributor_gstin_no',
        ),
        migrations.RemoveField(
            model_name='distributors',
            name='organization_name',
        ),
        migrations.AddField(
            model_name='distributors',
            name='distributor_name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]