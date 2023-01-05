from django.db import models

from django.core.files.base import ContentFile




# Create your models here.
class Hotel(models.Model):
    Main_Img = models.ImageField(upload_to='images/')