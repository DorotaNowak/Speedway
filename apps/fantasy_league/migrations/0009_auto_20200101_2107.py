# Generated by Django 2.2.6 on 2020-01-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy_league', '0008_auto_20200101_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='actual_play',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='actual_score',
            field=models.IntegerField(default=0),
        ),
    ]