from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
<<<<<<< HEAD
    path('usuarios/loguear/', views.loguear, name='loguear'),
    path('usuarios/logout/', LogoutView.as_view(template_name='usuario/salida.html'), name='salida'),
    path('usuarios/registro/', views.registro, name='registro'),
    path('usuarios/perfil/', views.ver_usuario, name='ver_usuario'),
    path('usuarios/perfil/editar', views.editar_usuario, name='editar_usuario'),
    path('usuarios/perfil/editar/password', views.CambiarPassword.as_view(), name='cambiar_pass'),
=======
    path('loguear/', views.loguear, name='loguear'),
    path('logout/', LogoutView.as_view(template_name='usuario/salida.html'), name='salida'),
    path('registro/', views.registro, name='registro'),
    path('perfil/editar', views.editar_usuario, name='editar_usuario'),
    path('perfil/editar/password', views.CambiarPassword.as_view(), name='cambiar_pass'),
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
]
