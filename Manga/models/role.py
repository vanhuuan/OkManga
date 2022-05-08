from django.db import models

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    role = models.CharField(max_length=10)

    def __str__(self):
        return "".join(self.role)