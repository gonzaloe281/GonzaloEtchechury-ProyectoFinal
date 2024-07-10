from django.db import models

class Vuelo(models.Model):
    vuelo = models.CharField(max_length=20)
    aerolinea = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    pasajeros = models.IntegerField()
<<<<<<< HEAD
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='imagenes_vuelos/', blank=True, null=True)
=======
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334

    def __str__(self):
        return f'''
    Vuelo {self.vuelo} de {self.aerolinea} con el {self.fabricante} {self.modelo}-{self.pasajeros}
<<<<<<< HEAD
    para el dia {self.fecha}
=======
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
    '''
