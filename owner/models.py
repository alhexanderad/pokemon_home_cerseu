from django.db import models

class Owner(models.Model):
  nombre = models.CharField(max_length=40)
  edad = models.IntegerField()
  pais = models.CharField(max_length=27, default='')
  dni = models.CharField(max_length=8, default=00000000)
  vigente = models.BooleanField(default=True)

  def __str__(self):
    return self.nombre