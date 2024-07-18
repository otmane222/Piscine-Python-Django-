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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ex09_planets'
        app_label = "ex09"
    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=64)
    birth_year = models.CharField(max_length=32, blank=True, null=True)
    gender = models.CharField(max_length=32, blank=True, null=True)
    eye_color = models.CharField(max_length=32, blank=True, null=True)
    hair_color = models.CharField(max_length=32, blank=True, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    # homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, to_field='name',null=True)
    homeworld = models.ForeignKey(Planets, default=1, verbose_name="Planets", on_delete=models.SET_DEFAULT, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ex09_people'
        app_label = "ex09"
    def __str__(self):
        return self.name