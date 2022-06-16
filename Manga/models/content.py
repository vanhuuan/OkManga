from django.db import models
from Manga.models.chapter import Chapter

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField()
    link = models.URLField()

    def __str__(self):
        return f"Page {self.index} - {str(self.chapter)} - {self.link}"
