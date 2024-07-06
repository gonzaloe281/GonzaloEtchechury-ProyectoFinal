from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('loguear/', views.loguear, name='loguear'),
    path('logout/', LogoutView.as_view(template_name='usuario/salida.html'), name='salida'),
    path('registro/', views.registro, name='registro'),
    path('perfil/editar', views.editar_usuario, name='editar_usuario'),
    path('perfil/editar/password', views.CambiarPassword.as_view(), name='cambiar_pass'),   
]
