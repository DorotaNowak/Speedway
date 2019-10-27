from django.db import models

# Create your models here.
class Player(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team=models.CharField(max_length=30)
    nationality=models.CharField(max_length=30)
    photo=models.ImageField()


