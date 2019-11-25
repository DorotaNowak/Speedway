# Generated by Django 2.2.6 on 2019-11-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy_league', '0002_player_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='team',
            name='budget',
            field=models.DecimalField(decimal_places=3, default=10.0, max_digits=6),
        ),
    ]