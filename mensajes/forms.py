from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    receptor = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None, label='Enviar a')

    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']
