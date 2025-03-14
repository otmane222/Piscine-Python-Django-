from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=64, null=False, unique=True)
    episode_nb = models.AutoField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    class Meta:
        db_table = 'ex05_movies'
        app_label = "ex05"
        # abstract = True
    def __str__(self):
        return self.title