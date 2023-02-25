from django.db import models

# Create your models here.
class Colleges(models.Model):
    college_id=models.IntegerField()
    location=models.CharField(max_length=100)
    name=models.CharField(max_length=1000)
