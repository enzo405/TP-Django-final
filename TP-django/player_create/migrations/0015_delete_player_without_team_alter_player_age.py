# Generated by Django 4.0.4 on 2022-05-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_create', '0014_alter_player_age_alter_player_nom_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Player_without_team',
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.CharField(choices=[('-18', '-18 ans'), ('+18 / -26', '+18 / -26'), ('+26', '+26 ans')], max_length=20),
        ),
    ]
