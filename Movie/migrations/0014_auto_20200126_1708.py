# Generated by Django 3.0.1 on 2020-01-26 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0013_auto_20200126_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='talk',
        ),
        migrations.AddField(
            model_name='showtime',
            name='talk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.Talkies'),
        ),
    ]
