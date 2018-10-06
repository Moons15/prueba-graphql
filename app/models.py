from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.name + ' '+ self.last_name
