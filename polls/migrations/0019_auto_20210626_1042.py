# Generated by Django 3.2.4 on 2021-06-26 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20210626_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mietzinseingaenge',
            name='datum',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 10, 42, 27, 362299)),
        ),
        migrations.AlterField(
            model_name='nebenkosten',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 10, 42, 27, 362299)),
        ),
        migrations.AlterField(
            model_name='nebenkosten',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 10, 42, 27, 362299)),
        ),
    ]
