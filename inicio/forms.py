from django import forms

class VueloFormularioBase(forms.Form):
    vuelo= forms.CharField(max_length=20)
    aerolinea= forms.CharField(max_length=30)
    fabricante= forms.CharField(max_length=20)
    modelo= forms.CharField(max_length=20)
    pasajeros= forms.IntegerField()
<<<<<<< HEAD
    fecha = forms.DateField(label="Fecha de vuelo", required=True,widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}))
    imagen = forms.ImageField(required=False)
=======
    
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
class EditarVueloFormulario(VueloFormularioBase):
    ...

class CrearVueloFormulario(VueloFormularioBase):
    ...
    
class BuscarVuelo(forms.Form):
    vuelo = forms.CharField(max_length=20, required=False)