from django import forms

class VueloFormularioBase(forms.Form):
    vuelo= forms.CharField(max_length=20)
    aerolinea= forms.CharField(max_length=30)
    fabricante= forms.CharField(max_length=20)
    modelo= forms.CharField(max_length=20)
    pasajeros= forms.IntegerField()
    
class EditarVueloFormulario(VueloFormularioBase):
    ...

class CrearVueloFormulario(VueloFormularioBase):
    ...
    
class BuscarVuelo(forms.Form):
    vuelo = forms.CharField(max_length=20, required=False)