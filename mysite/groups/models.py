from django.db import models

# Create your models here.

# class Group(models.Model):
#     #users = models.ArrayField(models.CharField(max_length=50), blank=True)
#     users = models.JSONField()
#     key = models.IntegerField()

class User(models.Model):
    email = models.CharField(max_length=50) # can change to email field later

    def __str__(self): # when querying db, it will list email, not id
        return self.email