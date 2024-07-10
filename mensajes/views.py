# En tu aplicación de mensajes (mensajes/views.py)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm

@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_envio')
    return render(request, 'mensajes/bandeja_entrada.html', {'mensajes_recibidos': mensajes_recibidos})



@login_required
def detalle_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id)
    if request.user == mensaje.receptor:
        if not mensaje.leido:
            mensaje.leido = True
            mensaje.save()
        if request.method == 'POST' and 'delete' in request.POST:
            mensaje.delete()
            messages.success(request, 'El mensaje ha sido eliminado.')
            return redirect('bandeja_entrada')
    return render(request, 'mensajes/detalle_mensaje.html', {'mensaje': mensaje})




@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        formulario = MensajeForm(request.POST)
        if formulario.is_valid():
            mensaje = formulario.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('bandeja_entrada')
    else:
        formulario = MensajeForm()
    return render(request, 'mensajes/enviar_mensaje.html', {'formulario': formulario})

