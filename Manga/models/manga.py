from django.db import models

from Manga.models.category import Category


class Manga(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, default="A great manga")
    category = models.ManyToManyField(Category)
    views = models.PositiveIntegerField(default=0)
    chapters_number = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_manga_by_id(mid):
        return Manga.objects.get(id=mid)

    @staticmethod
    def get_all_manga():
        return Manga.objects.all()

