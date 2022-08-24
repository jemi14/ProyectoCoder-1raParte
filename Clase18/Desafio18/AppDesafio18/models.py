from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fechaDeNacimiento= models.DateField()
    telefono= models.IntegerField()
    email= models.EmailField()
    estaVivo = models.BooleanField()
    peso = models.FloatField()


