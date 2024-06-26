# Generated by Django 5.0 on 2024-02-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand_app', '0127_cover_scrap_voucher_cover_scrap_particular1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='binding',
            name='total_remaining',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='binding',
            name='total_transfer_form',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='binding',
            name='transfer1',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cuttting',
            name='total_remaining',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cuttting',
            name='total_transfer_form',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cuttting',
            name='transfer1',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='gathering',
            name='total_remaining',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='gathering',
            name='total_transfer_form',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='gathering',
            name='transfer1',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='manual',
            name='total_remaining',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='manual',
            name='total_transfer_form',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='manual',
            name='transfer1',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pasting',
            name='total_remaining',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pasting',
            name='total_transfer_form',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pasting',
            name='transfer1',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='total_received_form_data',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='total_transfer_form',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form1',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form10',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form2',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form3',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form4',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form5',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form6',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form7',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form8',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='printing',
            name='transfer_total_form9',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='binding',
            name='transfer',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='binding',
            name='transfer_pending',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cuttting',
            name='transfer',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cuttting',
            name='transfer_pending',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gathering',
            name='transfer',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gathering',
            name='transfer_pending',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='manual',
            name='transfer',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='manual',
            name='transfer_pending',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pasting',
            name='transfer',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pasting',
            name='transfer_pending',
            field=models.CharField(default='0', max_length=200, null=True),
        ),
    ]
