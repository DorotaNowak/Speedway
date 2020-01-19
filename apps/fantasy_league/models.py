from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    team = models.CharField(max_length=10)
    nationality = models.CharField(max_length=10)
    price = models.IntegerField()
    actual_score = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + '    ' + 'cena:' +str(self.price) + '    ' + 'sredni wynik:'+str(self.actual_score)

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
    budget = models.IntegerField(default=500)
    score = models.IntegerField(default=0)

    def count_score(self):
        players = [self.player1, self.player2, self.player3, self.player4]
        self.score = 0
        for player in players:
            if player is not None:
                print(player.actual_score)
                self.score = self.score + player.actual_score
        return self.score


class League(models.Model):
    teams = models.ManyToManyField(Team)
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=1000, unique=True)
    password = models.CharField(max_length=1000)
