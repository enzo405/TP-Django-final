# Generated by Django 4.0.4 on 2022-05-11 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_create', '0008_player_without_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_models',
            name='budget',
            field=models.IntegerField(max_length=12),
        ),
    ]
