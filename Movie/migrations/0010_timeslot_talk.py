# Generated by Django 3.0.1 on 2020-01-26 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0009_auto_20200126_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='talk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.Talkies'),
        ),
    ]
