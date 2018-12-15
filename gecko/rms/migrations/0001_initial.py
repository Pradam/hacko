# Generated by Django 2.1.4 on 2018-12-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.PositiveIntegerField(choices=[(0, 'Inactive'), (2, 'Active')], default=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('aadhar_id', models.IntegerField(max_length=16)),
                ('name', models.TextField()),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'TRANSGENDER')])),
                ('age', models.PositiveIntegerField()),
                ('premium', models.PositiveIntegerField()),
                ('coverage', models.PositiveIntegerField()),
                ('is_alcoholic', models.IntegerField(choices=[(1, 'NO'), (2, 'OCCATIONALLY'), (3, 'HEAVY')], default=1)),
                ('is_smoker', models.IntegerField(choices=[(1, 'NO'), (2, 'MODERATE'), (3, 'CHAIN')], default=1)),
                ('claimed', models.IntegerField(choices=[(1, 'NO CLAIM'), (2, 'REJECTED'), (3, 'ACCEPTED')], default=1)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='historydata',
            unique_together={('aadhar_id',)},
        ),
    ]