from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
  class Generation(models.IntegerChoices):
    PRIMERA = 1
    SEGUNDA = 2
    TERCERA = 3

  nombre = models.CharField(max_length=40)
  tipo = models.CharField(max_length=50)
  generacion = models.IntegerField(choices=Generation.choices)
  fecha_creacion = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.nombre