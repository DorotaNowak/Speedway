# Generated by Django 2.2.6 on 2019-11-24 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fantasy_league', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('team', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=6, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('budget', models.DecimalField(decimal_places=6, default=10.0, max_digits=6)),
                ('player1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player1', to='fantasy_league.Player')),
                ('player2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player2', to='fantasy_league.Player')),
                ('player3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player3', to='fantasy_league.Player')),
                ('player4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player4', to='fantasy_league.Player')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
