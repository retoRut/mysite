# Generated by Django 3.2.4 on 2021-06-26 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20210626_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mietzinseingaenge',
            name='datum',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 9, 21, 47, 133369)),
        ),
        migrations.AlterField(
            model_name='nebenkosten',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 9, 21, 47, 133369)),
        ),
        migrations.AlterField(
            model_name='nebenkosten',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 9, 21, 47, 133369)),
        ),
        migrations.AlterField(
            model_name='zahlungstyp',
            name='typ',
            field=models.CharField(max_length=50),
        ),
    ]
