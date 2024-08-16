from django.db import models

# Create your models here.

class link(models.Model):
    address = models.CharField(max_length=1000)
    aid = models.CharField(max_length=100)
    