#Configurando redireccionamiento 
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    #GENERO
    path('listadoGeneros/', views.listadoGeneros,name='listadoGeneros'),
    path('eliminarGenero/<id>', views.eliminarGenero,name='eliminarGenero'),
    path('nuevoGenero/', views.nuevoGenero,name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero,name='guardarGenero'),
    path('editarGenero/<id>', views.editarGenero,name='editarGenero'),
    path('procesarActualizacionPis/', views.procesarActualizacionGenero,name='procesarActualizacionGenero'),
    #PAIS
    path('listadoPais/', views.listadoPais, name='listadoPais'),
    path('nuevoPais/', views.nuevoPais,name='nuevoPais'),
    path('guardarPais/', views.guardarPais,name='guardarPais'),
    path('editarPais/<id>', views.editarPais,name='editarPais'),
    path('eliminarPais/<id>', views.eliminarPais,name='eliminarPais'),
    path('procesarActualizacionPais/', views.procesarActualizacionPais,name='procesarActualizacionPais'),

    #DIRECTORES 
    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path('nuevoDirector/', views.nuevoDirector,name='nuevoDirector'),
    path('guardarDirector/', views.guardarDirector,name='guardarDirector'),
    path('editarDirector/<id>', views.editarDirector,name='editarDirector'),
    path('eliminarDirector/<id>', views.eliminarDirector,name='eliminarDirector'),
    path('gestionDirectores/',views.gestionDirectores, name='gestionDirectores'),
    path('procesarActualizacionDirector/', views.procesarActualizacionDirector,name='procesarActualizacionDirector'),

     #PELICULAS
    path('gestionPelicula/',views.gestionPelicula, name='gestionPelicula'), 
    path('guardarPelicula/',views.guardarPelicula, name='guardarPelicula'), 
    path('listadoPeliculas/',views.listadoPeliculas, name='listadoPeliculas'), 

    #CINE
    path('listadoCines/', views.listadoCines, name='listadoCines'),
    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/', views.guardarCine,name='guardarCine'),
    path('gestionPelicula/',views.gestionPelicula, name='gestionPelicula'),
]