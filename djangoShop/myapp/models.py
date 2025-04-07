from django.db import models

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=64)
    dob = models.DateField()
    price = models.IntegerField()