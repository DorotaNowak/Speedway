from django.db import models



class Player2(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team=models.CharField(max_length=30)
    nationality=models.CharField(max_length=30)
    price=models.FloatField()
class Player3(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team=models.CharField(max_length=30)
    nationality=models.CharField(max_length=30)
    price=models.FloatField()
