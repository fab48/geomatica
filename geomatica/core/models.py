from django.db import models
from PIL import Image

# Create your models here.

class Hueco(models.Model):
    direccion = models.CharField(max_length=200)
    latitud = models.FloatField(default=0.0)
    longitud = models.FloatField(default=0.0)
    foto = models.ImageField(upload_to = 'hueco')

class Trafico(models.Model):
    zona = models.CharField(max_length=200)
    nivel = models.IntegerField(default=1)
