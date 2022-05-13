# Generated by Django 4.0.4 on 2022-05-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_create', '0013_alter_player_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.CharField(choices=[('-18', '-18 ans'), ('entre 18 et 26', 'entre 18 et 26'), ('+26', '+26 ans')], max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='nom',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='player_without_team',
            name='age',
            field=models.CharField(choices=[('-18', '-18 ans'), ('entre 18 et 26', 'entre 18 et 26'), ('+26', '+26 ans')], max_length=20),
        ),
        migrations.AlterField(
            model_name='player_without_team',
            name='nom',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='team_models',
            name='nom',
            field=models.CharField(max_length=10),
        ),
    ]
