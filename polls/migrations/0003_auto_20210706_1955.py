# Generated by Django 3.2.4 on 2021-07-06 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_mieter_mietobjekt_mietobjektsummary_mietzins_mietzinseingaenge_mietzinseingaengesummary_mietzinsprof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mietzins',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 6, 19, 55, 50, 823784)),
        ),
        migrations.AlterField(
            model_name='mietzins',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 6, 19, 55, 50, 823784)),
        ),
        migrations.AlterField(
            model_name='mietzinseingaenge',
            name='datum',
            field=models.DateField(default=datetime.datetime(2021, 7, 6, 19, 55, 50, 830781)),
        ),
        migrations.AlterField(
            model_name='mietzinsprofil',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 6, 19, 55, 50, 825783)),
        ),
        migrations.AlterField(
            model_name='mietzinsprofil',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 6, 19, 55, 50, 825783)),
        ),
    ]
