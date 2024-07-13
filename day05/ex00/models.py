from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=64, null=False, unique=True)
    episode_nb = models.AutoField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    class Meta:
        db_table = 'ex00_movies'