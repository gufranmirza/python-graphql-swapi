from django.db import models

# Create your models here.

# cookbook/ingredients/models.py
from django.db import models


class Human(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=1024)
    appears_in = models.CharField(max_length=1024)
    home_planet = models.CharField(max_length=1024)
    height = models.IntegerField()

    def __str__(self):
        return self.name