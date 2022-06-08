from django.db import models

from Manga.models.manga import Manga


class Chapter(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    modified_date = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {str(self.manga)}"
