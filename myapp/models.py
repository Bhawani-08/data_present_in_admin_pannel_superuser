from django.db import models
# Create your models here.

class mymodel(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname  = models.CharField(max_length = 255)
    salary = models.IntegerField()

