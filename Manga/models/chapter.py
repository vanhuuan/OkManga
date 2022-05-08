from django.db import models

from Manga.models.comic import Comic


class Chapter(models.Model):
    id_chap = models.AutoField(primary_key=True)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    name_chap = models.CharField(max_length=100)
    ordinal_chap = models.IntegerField()
    date_release = models.DateField()
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.name_chap
