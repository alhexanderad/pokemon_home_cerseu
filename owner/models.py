from django.db import models

class Owner(models.Model):
  nombre = models.CharField(max_length=40)
  pais = models.CharField(max_length=27)
  descripcion = models.TextField()