from django.db import models
from django.utils import timezone

# Create your models here.

# class Movies07(models.Model):
#     title = models.CharField(max_length=64, null=False, unique=True)
#     episode_nb = models.AutoField(primary_key=True)
#     opening_crawl = models.TextField(null=True)
#     director = models.CharField(max_length=32, null=False)
#     producer = models.CharField(max_length=128, null=False)
#     release_date = models.DateField(null=False)
#     created = models.DateTimeField(default=timezone.now())
#     updated = models.DateTimeField(default=timezone.now())

#     def update_opening_crawl(self, new_opening_crawl):
#         self.opening_crawl = new_opening_crawl
#         self.updated = timezone.now()  # Update the 'updated' timestamp to current time
#         self.save()
    
#     class Meta:
#         db_table = 'ex07_movies'
#         app_label = "ex07"
#         # abstract = True
#     def __str__(self):
#         return self.title