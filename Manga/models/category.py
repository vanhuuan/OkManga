from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category