from django.db import models

from Manga.models.genre import Genre

class Manga(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    thumbnail = models.URLField()
    status = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True)
    genres = models.ManyToManyField(Genre)
    views = models.PositiveIntegerField(default=0)
    chapters_number = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

