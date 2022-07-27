from django.db import models

# Create your models here.
class Message(models.Model):
    fullName = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

