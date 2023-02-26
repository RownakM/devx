from django.db import models

# Create your models here.
class Domain(models.Model):
    domain=models.CharField(max_length=1000)

class email(models.Model):
    email_user=models.CharField(max_length=1000)

class Mail(models.Model):
    from_mail=models.CharField(max_length=1000)
    to_mail=models.CharField(max_length=1000)
    subject=models.CharField(max_length=1000)
    content=models.TextField()
