from django.db import models

# Create your models here.
class PhotoUploader(models.Model):
    name = models.CharField(max_length =120, default = " ")
    image = models.ImageField()
