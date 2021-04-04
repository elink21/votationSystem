from django.db import models

# Create your models here.
class django_system(models.Model):
    name= models.CharField(max_length=30)
    password= models.CharField(max_length=30)
    vote= models.CharField(max_length=30)


class UserEncrypted(models.Model):
    name= models.CharField(max_length=30)
    password= models.CharField(max_length=30)
    vote= models.CharField(max_length=30)
