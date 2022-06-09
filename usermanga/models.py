from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from Manga.models.manga import Manga


class UserManga(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

    @staticmethod
    def get_all_user_manga(uid):
        rs = []
        listId = UserManga.objects.filter(userId_id=uid)
        for i in listId:
            rs.append(Manga.get_manga_by_id(i.manga.id))
        return rs
