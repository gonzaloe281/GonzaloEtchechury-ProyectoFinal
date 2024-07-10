<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
=======
from django.shortcuts import render, redirect
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader
<<<<<<< HEAD
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from inicio.models import Vuelo
from .forms import CrearVueloFormulario, BuscarVuelo, EditarVueloFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
=======

from inicio.models import Vuelo
from .forms import CrearVueloFormulario, BuscarVuelo, EditarVueloFormulario

>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/index.html')

<<<<<<< HEAD
def crear_vuelo_v1(request, nombrevuelo, aerolinea, fabricante, modelo, pasajeros, fecha):
    vuelo = Vuelo(nombrevuelo=nombrevuelo, aerolinea=aerolinea, fabricante=fabricante, modelo=modelo, pasajeros=pasajeros, fecha=fecha)
=======
def crear_vuelo_v1(request, nombrevuelo, aerolinea, fabricante, modelo, pasajeros):
    vuelo = Vuelo(nombrevuelo=nombrevuelo, aerolinea=aerolinea, fabricante=fabricante, modelo=modelo, pasajeros=pasajeros)
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
    vuelo.save()
    return render(request, 'inicio/crear_vuelo.html', {'vuelo': vuelo})

def crear_vuelo(request):
<<<<<<< HEAD
    if request.method == 'POST':
        formulario = CrearVueloFormulario(request.POST, request.FILES)
=======
    formulario = CrearVueloFormulario()
    if request.method == 'POST':
        formulario = CrearVueloFormulario(request.POST)
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
        if formulario.is_valid():
            datos = formulario.cleaned_data
            vuelo = Vuelo(
                vuelo=datos.get('vuelo'),
                aerolinea=datos.get('aerolinea'),
                fabricante=datos.get('fabricante'),
                modelo=datos.get('modelo'),
<<<<<<< HEAD
                pasajeros=datos.get('pasajeros'),
                fecha=datos.get('fecha'),
                imagen=datos.get('imagen') if 'imagen' in request.FILES else None
            )
            vuelo.save()
            return redirect('listado')
    else:
        formulario = CrearVueloFormulario()
    return render(request, 'inicio/crear_vuelo.html', {'formulario': formulario})


@login_required
=======
                pasajeros=datos.get('pasajeros')
            )
            vuelo.save()
            return redirect('listado')
    return render(request, 'inicio/crear_vuelo.html', {'formulario': formulario})

>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
def eliminar_vuelo(request, id):
    vuelo = Vuelo.objects.get(id=id)
    vuelo.delete()
    return redirect('listado')

<<<<<<< HEAD
@login_required
def editar_vuelo(request, id):
    vuelo = get_object_or_404(Vuelo, id=id)
    if request.method == 'POST':
        formulario = EditarVueloFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            vuelo.vuelo = datos.get('vuelo')
            vuelo.aerolinea = datos.get('aerolinea')
            vuelo.fabricante = datos.get('fabricante')
            vuelo.modelo = datos.get('modelo')
            vuelo.pasajeros = datos.get('pasajeros')
            vuelo.fecha = datos.get('fecha')
            if 'imagen' in request.FILES:
                vuelo.imagen = datos.get('imagen')
            vuelo.save()
            return redirect('listado')
    else:
        formulario = EditarVueloFormulario(initial={
            'vuelo': vuelo.vuelo,
            'aerolinea': vuelo.aerolinea,
            'fabricante': vuelo.fabricante,
            'modelo': vuelo.modelo,
            'pasajeros': vuelo.pasajeros,
            'fecha': vuelo.fecha,
            'imagen': vuelo.imagen,
        })
    return render(request, 'inicio/editar_vuelo.html', {'formulario': formulario, 'vuelo': vuelo})


=======
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

>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
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
