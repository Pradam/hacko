# Generated by Django 2.1.4 on 2018-12-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0005_remove_historydata_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydata',
            name='aadhar_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='historydata',
            name='coverage',
            field=models.BigIntegerField(),
        ),
    ]
