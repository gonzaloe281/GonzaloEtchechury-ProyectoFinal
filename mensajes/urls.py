from django.urls import path
from . import views
from mensajes import views as mensajes_views

urlpatterns = [
    path('bandeja_entrada/', mensajes_views.bandeja_entrada, name='bandeja_entrada'),
    path('enviar/', mensajes_views.enviar_mensaje, name='enviar_mensaje'),
    path('detalle_mensaje/<int:mensaje_id>/', mensajes_views.detalle_mensaje, name='detalle_mensaje'),
]
