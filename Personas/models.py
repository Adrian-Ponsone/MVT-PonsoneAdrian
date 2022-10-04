from django.db import models
from datetime import datetime

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_de_creacion = models.DateField(null=True)