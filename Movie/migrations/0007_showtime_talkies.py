# Generated by Django 3.0.1 on 2020-01-25 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0006_auto_20200120_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talkies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.MovieDetails')),
                ('talk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.Talkies')),
            ],
        ),
    ]