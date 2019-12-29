from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    team = models.CharField(max_length=10)
    nationality = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    # return path to player's image
    def get_path(self):
        return 'photos/players/' + self.last_name + '_' + self.first_name + '.jpg'


# related name  - user can access this by user.team
class Team(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team', null=True)
    player1 = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='player1', null=True)
    player2 = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='player2', null=True)
    player3 = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='player3', null=True)
    player4 = models.ForeignKey(Player, on_delete=models.DO_NOTHING, related_name='player4', null=True)
    budget = models.DecimalField(default=10.0, max_digits=6, decimal_places=3)
