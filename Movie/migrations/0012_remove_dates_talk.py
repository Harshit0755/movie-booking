# Generated by Django 3.0.1 on 2020-01-26 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0011_auto_20200126_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dates',
            name='talk',
        ),
    ]
