from django.db import models

# Create your models here.

class Img(models.Model):
    name = models.CharField(default="plain_image", max_length=50)
    img = models.ImageField(upload_to='images/')
    secret_img = models.ImageField(upload_to='secret_images/')

class EncodedImg(models.Model):
    name = models.CharField(max_length=50)
    encoded_img = models.ImageField(upload_to='encoded_images/')