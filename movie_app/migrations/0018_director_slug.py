# Generated by Django 4.1.2 on 2022-11-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0017_remove_director_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='slug',
            field=models.SlugField(default=None),

        ),
    ]
