# Generated by Django 4.1.5 on 2023-08-07 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_remove_extraform_id_alter_extraform_form1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extraform',
            old_name='brand_name',
            new_name='brand_name_1',
        ),
        migrations.RenameField(
            model_name='extraform',
            old_name='medium',
            new_name='class_name_1',
        ),
        migrations.RenameField(
            model_name='extraform',
            old_name='standard',
            new_name='medium_1',
        ),
        migrations.RenameField(
            model_name='extraform',
            old_name='subject',
            new_name='subject_1',
        ),
    ]
