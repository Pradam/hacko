# Generated by Django 2.1.4 on 2018-12-15 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0003_historydata_is_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydata',
            name='is_member',
            field=models.IntegerField(choices=[(1, 'YES'), (2, 'NO'), (3, 'PENDING')], default=1),
        ),
    ]