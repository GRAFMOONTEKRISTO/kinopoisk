# Generated by Django 4.1.2 on 2022-11-16 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0016_director_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='slug',
        ),
    ]
