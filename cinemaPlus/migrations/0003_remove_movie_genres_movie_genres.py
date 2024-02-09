# Generated by Django 5.0.2 on 2024-02-09 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinemaPlus", "0002_actor_remove_director_biography_play_delete_review"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="genres",
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cinemaPlus.genre",
            ),
        ),
    ]
