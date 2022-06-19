from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='authentication/avatar')

    def save(self, *args, **kwargs):
        try:
            this = Avatar.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except:
            pass
        super(Avatar, self).save(*args, **kwargs)
