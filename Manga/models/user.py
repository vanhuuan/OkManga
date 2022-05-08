from django.db import models
from Manga.models.role import Role


class User(models.Model):
    id_user = models.AutoField(auto_created=True, primary_key=True)
    user_name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    gender = models.BooleanField(null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
