from django.db import models
from Manga.models.chapter import Chapter


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    chap = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    url = models.URLField()
