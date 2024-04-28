from django.db import models

# Create your models here.

class Img(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')
    secret_msg = models.CharField(max_length=100)

class EncodedImg(models.Model):
    name = models.CharField(max_length=50)
    encoded_img = models.ImageField(upload_to='encoded_images/')