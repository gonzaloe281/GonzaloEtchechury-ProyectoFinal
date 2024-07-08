from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Pasajero
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Pasajeros(ListView):
    model = Pasajero
    template_name = 'persona/listado_de_pasajeros.html'
    context_object_name = 'pasajeros'
    
class CrearPasajero(CreateView):
    model = Pasajero
    template_name = 'persona/crear_pasajero.html'
    success_url = reverse_lazy('pasajeros')
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'documento', 'ciudad']
    
class EditarPasajero(LoginRequiredMixin, UpdateView):
    model = Pasajero
    template_name = 'persona/editar_pasajero.html'
    success_url = reverse_lazy('pasajeros')
    fields = ['nombre', 'apellido', 'fecha_nacimiento', 'documento', 'ciudad']
    
class VerPasajero(DetailView):
    model = Pasajero
    template_name = 'persona/ver_pasajero.html'
    
class EliminarPasajero(LoginRequiredMixin, DeleteView):
    model = Pasajero
    template_name = "persona/eliminar_pasajero.html"
    success_url = reverse_lazy('pasajeros')