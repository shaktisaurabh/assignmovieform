from django.db import models

# Create your models here.
class project(models.Model):
    name= models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    
