from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from inicio.models import Vuelo
from .forms import CrearVueloFormulario, BuscarVuelo, EditarVueloFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/index.html')

def crear_vuelo_v1(request, nombrevuelo, aerolinea, fabricante, modelo, pasajeros):
    vuelo = Vuelo(nombrevuelo=nombrevuelo, aerolinea=aerolinea, fabricante=fabricante, modelo=modelo, pasajeros=pasajeros)
    vuelo.save()
    return render(request, 'inicio/crear_vuelo.html', {'vuelo': vuelo})

def crear_vuelo(request):
    formulario = CrearVueloFormulario()
    if request.method == 'POST':
        formulario = CrearVueloFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            vuelo = Vuelo(
                vuelo=datos.get('vuelo'),
                aerolinea=datos.get('aerolinea'),
                fabricante=datos.get('fabricante'),
                modelo=datos.get('modelo'),
                pasajeros=datos.get('pasajeros')
            )
            vuelo.save()
            return redirect('listado')
    return render(request, 'inicio/crear_vuelo.html', {'formulario': formulario})

@login_required
def eliminar_vuelo(request, id):
    vuelo = Vuelo.objects.get(id=id)
    vuelo.delete()
    return redirect('listado')

@login_required
def editar_vuelo(request, id):
    vuelo = Vuelo.objects.get(id=id)
    formulario = EditarVueloFormulario(initial={'vuelo': vuelo.vuelo, 'aerolinea': vuelo.aerolinea, 'fabricante': vuelo.fabricante, 'modelo': vuelo.modelo, 'pasajeros': vuelo.pasajeros})
    if request.method == 'POST':
        formulario = EditarVueloFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            vuelo.vuelo = info['vuelo']
            vuelo.aerolinea = info['aerolinea']
            vuelo.fabricante = info['fabricante']
            vuelo.modelo = info['modelo']
            vuelo.pasajeros = info['pasajeros']
            vuelo.save()
            return redirect('listado')
    return render(request, 'inicio/editar_vuelo.html', {'formulario': formulario, 'vuelo': vuelo})

def listado(request):
    formulario = BuscarVuelo()
    vuelos = Vuelo.objects.all()
    if request.method == 'GET' and 'vuelo' in request.GET:
        formulario = BuscarVuelo(request.GET)
        if formulario.is_valid():
            vuelo_nombre = formulario.cleaned_data.get('vuelo')
            if vuelo_nombre:
                vuelos = Vuelo.objects.filter(vuelo__icontains=vuelo_nombre)
    return render(request, 'inicio/listado.html', {'vuelos': vuelos, 'formulario': formulario})

def ver_vuelo(request, id):
    vuelo_instancia = Vuelo.objects.get(id=id)
    return render(request, 'inicio/ver_vuelo.html', {'vuelo': vuelo_instancia})

def about(request):
    return render(request, 'inicio/acerca_de.html')
