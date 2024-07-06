from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # path('vuelos/crear/<str:nombrevuelo>/<str:aerolinea>/<str:fabricante>/<str:modelo>/<int:pasajeros>', views.crear_vuelo, name='crear_vuelo'),
    path('vuelos/', views.listado, name='listado'),
    path('vuelos/crear/', views.crear_vuelo, name='crear_vuelo'),
    path('about/', views.about, name='about'),
    path('vuelos/editar/<int:id>/', views.editar_vuelo, name='editar_vuelo'),
    path('vuelos/eliminar/<int:id>/', views.eliminar_vuelo, name='eliminar_vuelo'),
    path('vuelos/<int:id>/', views.ver_vuelo, name='ver_vuelo'),
    
    
    
    
    
]
