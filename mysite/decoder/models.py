from django.db import models

# Create your models here.

class SecretMessage(models.Model):
    secret_msg = models.CharField(max_length=100)
    secret_img = models.ImageField(upload_to='decoded_images/')

class ImgToDecode(models.Model):
    img = models.ImageField(upload_to='images_to_decode/')