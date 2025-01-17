from django.db import models

class Vuelo(models.Model):
    vuelo = models.CharField(max_length=20)
    aerolinea = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    pasajeros = models.IntegerField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imagenes_vuelos/', blank=True, null=True)

    def __str__(self):
        return f'''
    Vuelo {self.vuelo} de {self.aerolinea} con el {self.fabricante} {self.modelo}-{self.pasajeros}
    para el dia {self.fecha}
    '''
