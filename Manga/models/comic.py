from django.db import models

from Manga.models.genre import Genre


class Comic(models.Model):
    id_comic = models.AutoField(primary_key=True)
    name_comic = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    genres = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_release = models.DateField()
    status = models.CharField(max_length=20)
    num_chapter = models.IntegerField()
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.name_comic