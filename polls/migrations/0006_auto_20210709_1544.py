# Generated by Django 3.2.4 on 2021-07-09 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210706_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unterhalt',
            old_name='mietobjekt',
            new_name='mietobject',
        ),
        migrations.AlterField(
            model_name='mietzins',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 15, 44, 16, 596509)),
        ),
        migrations.AlterField(
            model_name='mietzins',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 15, 44, 16, 596509)),
        ),
        migrations.AlterField(
            model_name='mietzinseingaenge',
            name='datum',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 15, 44, 16, 605504)),
        ),
        migrations.AlterField(
            model_name='mietzinsprofil',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 15, 44, 16, 598507)),
        ),
        migrations.AlterField(
            model_name='mietzinsprofil',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 15, 44, 16, 598507)),
        ),
        migrations.AlterField(
            model_name='unterhalt',
            name='betrag',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Investition (SFR)'),
        ),
        migrations.AlterField(
            model_name='unterhalt',
            name='project',
            field=models.CharField(max_length=200, verbose_name='Projekt'),
        ),
    ]
