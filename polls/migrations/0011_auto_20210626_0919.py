# Generated by Django 3.2.4 on 2021-06-26 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20210626_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mietzinseingaenge',
            name='datum',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 9, 19, 55, 531556)),
        ),
        migrations.AlterField(
            model_name='nebenkosten',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 9, 19, 55, 531556)),
        ),
        migrations.AlterField(
            model_name='nebenkosten',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 9, 19, 55, 531556)),
        ),
        migrations.AlterField(
            model_name='zahlungstyp',
            name='typ',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
