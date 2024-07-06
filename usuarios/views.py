from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioDeRegistro, EditarUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import MetaDataUsuarios

# Create your views here.
def loguear(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
        
            user = authenticate(request, username=usuario, password=contrasenia)

            django_login(request, user)
            
            MetaDataUsuarios.objects.get_or_create(user=user)

            return redirect('inicio')
    
    return render(request, 'usuario/logueo.html', {'formulario': formulario})

def registro(request):
    
    formulario = FormularioDeRegistro()
    
    if request.method == "POST":
        formulario = FormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('loguear')
    
    return render(request, 'usuario/registro.html', {'formulario': formulario})

@login_required
def editar_usuario(request):
    
    metadatausuarios = request.user.metadatausuarios
    formulario = EditarUsuario(initial={'avatar': metadatausuarios.avatar}, instance=request.user)
    
    if request.method == "POST":
        formulario = EditarUsuario(request.POST, request.FILES , instance=request.user)
        if formulario.is_valid():
            
            
            metadatausuarios.avatar = formulario.cleaned_data.get('avatar')
            metadatausuarios.save()
            
            formulario.save()
            return redirect('editar_usuario')
    
    return render(request, 'usuario/editar_usuario.html', {'formulario': formulario})

class CambiarPassword(PasswordChangeView):
    template_name = 'usuario/cambiar_pass.html'
    success_url = reverse_lazy('editar_usuario')