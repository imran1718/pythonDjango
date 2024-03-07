from django.db import models

# Create your models here.
class formvalidation(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField()
    age= models.IntegerField()
    password=models.CharField(max_length=50,unique=True,default=True)

    def __str__(self):
        return f"{self.name} ({self.email})"