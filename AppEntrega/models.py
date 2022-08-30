from django.db import models

# Create your models here.
class Deportes(models.Model):
    nombre = models.CharField(max_length= 50)
    turno = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+self.turno

class Profesores(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField()
    profesion = models.CharField(max_length = 30)

class Socios(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    dni= models.IntegerField()
    email = models.EmailField()
