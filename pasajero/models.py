from django.db import models


# Create your models here.
class Pasajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=250)
    fecha_nacimiento = models.DateField()
    documento = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'