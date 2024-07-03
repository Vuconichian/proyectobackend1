from django.db import models

# Create your models here.


class Futbolista(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    team = models.CharField(max_length=128)
    worldchampion = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Director(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    team = models.CharField(max_length=128)
    worldchampion = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.name}'
    
class Estadio(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    capacity = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id} - {self.name}'

class User(models.Model):
    name = models.CharField(max_length=128)
    futbolistas = models.ManyToManyField(Futbolista, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    estadios = models.ManyToManyField(Estadio, blank=True)

    def __str__(self):
        return self.name