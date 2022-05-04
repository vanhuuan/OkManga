from django.db import models

# Create your models here.
class Role(models.Model):
    id_role=models.AutoField(primary_key=True)
    role=models.CharField(max_length=10)
    
    def __str__(self):
        return "".join(self.role)

class User(models.Model):
    id_user=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.BooleanField()
    email=models.EmailField()
    def __str__(self):
        return self.name
    
class Comic(models.Model):
    id_comic=models.CharField(max_length=10,primary_key=True)
    name_comic=models.CharField(max_length=50)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    date_release=models.DateField()
    status=models.CharField(max_length=20)
    num_chapter=models.IntegerField()
    views= models.IntegerField()
    def __str__(self):
        return self.name_comic

class Chapter(models.Model):
    id_chap=models.CharField(max_length=10,primary_key=True)
    comic=models.ForeignKey(Comic,on_delete=models.CASCADE)
    name_chap=models.CharField(max_length=100)
    ordinal_chap=models.IntegerField()
    date_release=models.DateField()
    views=models.IntegerField()
    def __str__(self):
        return self.name_chap

class Content(models.Model):
    id=models.IntegerField(primary_key=True)
    chap=models.ForeignKey(Chapter,on_delete=models.CASCADE)
    url=models.URLField()
    

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    chap=models.ForeignKey(Chapter,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
