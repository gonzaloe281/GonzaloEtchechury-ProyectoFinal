from django.urls import path
from . import views

urlpatterns = [
    path('pasajeros/', views.Pasajeros.as_view(), name='pasajeros'),
    path('pasajeros/crear/', views.CrearPasajero.as_view(), name='crear_pasajero'),
    path('pasajeros/<int:pk>/', views.VerPasajero.as_view(), name='ver_pasajero'),
    path('pasajeros/<int:pk>/editar/', views.EditarPasajero.as_view(), name='editar_pasajero'),
    path('pasajeros/<int:pk>/eliminar/', views.EliminarPasajero.as_view(), name='eliminar_pasajero'),
]
