from django.db import models

from Manga.models.genre import Genre
from Manga.models.user import User


class Comic(models.Model):
    id_comic = models.AutoField(primary_key=True)
    name_comic = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    genres = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_release = models.DateField()
    status = models.CharField(max_length=20)
    num_chapter = models.IntegerField()
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.name_comic

    @staticmethod
    def get_comic_by_id(ids):
        return Comic.objects.filter(id_comic=ids)

    @staticmethod
    def get_comics_by_poster_id(uid):
        return Comic.objects.filter(poster=uid)

