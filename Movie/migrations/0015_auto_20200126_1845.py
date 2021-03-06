# Generated by Django 3.0.1 on 2020-01-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0014_auto_20200126_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='times',
            name='date',
        ),
        migrations.RemoveField(
            model_name='times',
            name='show',
        ),
        migrations.RemoveField(
            model_name='times',
            name='talk',
        ),
        migrations.AddField(
            model_name='showtime',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='showtime',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='showtime',
            name='time1',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='showtime',
            name='time2',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='showtime',
            name='time3',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='dates',
        ),
        migrations.DeleteModel(
            name='times',
        ),
    ]
