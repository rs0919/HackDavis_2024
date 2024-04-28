from django.db import models

# Create your models here.

class Group(models.Model):
    users = models.ArrayField()
    key = models.IntegerField()