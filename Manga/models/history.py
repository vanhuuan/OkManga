from django.db import models

from Manga.models.chapter import Chapter
from django.contrib.auth.models import User


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    comment = models.CharField(max_length=200)
