from django.db import models

from django.utils import timezone

# Create your models here.



class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.CharField(max_length=255, blank=True, null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.CharField(max_length=128, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'ex10_planets'
        app_label = "ex10"

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=64, null=True)
    birth_year = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=32, blank=True, null=True)
    eye_color = models.CharField(max_length=32, blank=True, null=True)
    hair_color = models.CharField(max_length=32, blank=True, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey('Planets', on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = 'ex10_people'
        app_label = "ex10"

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(max_length=64, null=False, unique=True)
    episode_nb = models.AutoField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    characters = models.ManyToManyField('People', related_name='movies')

    class Meta:
        db_table = 'ex10_movies'
        app_label = "ex10"
    def __str__(self):
        return self.title
