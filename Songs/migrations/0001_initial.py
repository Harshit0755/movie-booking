# Generated by Django 3.0.1 on 2020-01-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
                ('comany', models.CharField(max_length=50)),
            ],
        ),
    ]
