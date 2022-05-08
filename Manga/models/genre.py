from django.db import models


class Genre(models.Model):
    GenreID = models.AutoField(primary_key=True)
    Genre = models.CharField(max_length=50)

    def __str__(self):
        return self.Genre
