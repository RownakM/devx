from django.db import models

# Create your models here.
class Colleges(models.Model):
    college_id=models.IntegerField()
    location=models.CharField(max_length=100)
    name=models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural="Colleges"


STATUS_CHOICES=(
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Rejected','Rejected')
)

class Application(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField()
    whatsapp_number=models.CharField(max_length=1000)
    college=models.ForeignKey(Colleges,on_delete=models.CASCADE)
    linkedin=models.URLField()
    github=models.URLField()
    question=models.TextField()
    meal_type=models.CharField(max_length=1000)
    tshirt_size=models.CharField(max_length=1000)
    status=models.CharField(max_length=1000,choices=STATUS_CHOICES,default="Pending")
    created_date=models.DateTimeField(auto_now_add=True)