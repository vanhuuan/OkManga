from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User # new


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # new
    title = models.CharField(max_length=50)
    body = models.TextField()