# Generated by Django 4.0.4 on 2022-05-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_create', '0010_alter_player_nom_alter_player_prix_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='prix',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='player_without_team',
            name='prix',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='team_models',
            name='budget',
            field=models.IntegerField(),
        ),
    ]