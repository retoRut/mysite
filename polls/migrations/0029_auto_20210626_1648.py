# Generated by Django 3.2.4 on 2021-06-26 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_auto_20210626_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mietzinseingaenge',
            name='datum',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 16, 48, 39, 342727)),
        ),
        migrations.AlterField(
            model_name='nebenkosten',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 16, 48, 39, 342727)),
        ),
        migrations.AlterField(
            model_name='nebenkosten',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 16, 48, 39, 342727)),
        ),
    ]
