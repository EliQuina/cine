from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Genero, Director, Pelicula,Pais,Cine
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return render(request,"home.html")
# crearemos una nueva vista
def listadoPeliculas(request):
    #crear una nueva variable 
    peliculasBdd=Pelicula.objects.all()
    return render(request,"listadoPeliculas.html", {'peliculas' : peliculasBdd}) 
def listadoDirectores(request):
    #crear una nueva variable 
    directoresBdd=Director.objects.all()
    return render(request,"listadoDirectores.html", {'directores' : directoresBdd}) 

#------------------------------Genero--------------------------------
#renderizando el template listadoGeneros
def listadoGeneros(request):
    #crear una nueva variable 
    generosBdd=Genero.objects.all()
    return render(request,"listadoGeneros.html", {'generos' : generosBdd}) 
#Se recibe el id para eliminar 
def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, "Género eliminado Correctamente")
    return redirect('/listadoGeneros')
#renderizando formulario de nuevo Género
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')
#Insertando Genero en la base de datos 
def guardarGenero(request):
    nom=request.POST["nombre"]
    des=request.POST["descripcion"]
    fot=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request, "Género registrado exitosamente")
    return redirect('listadoGeneros')
#Renderozando formulario de actualización 
def editarGenero(request, id):
    generoEditar=Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar':generoEditar})
#Actualizando nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request, 'Genero actualizado exitosamente.')
    return redirect('listadoGeneros')

#-----------------------------Pais--------------------------------------------------------------
#crear una nueva variable 
def listadoPais(request):
    paisBdd=Pais.objects.all()
    return render(request,"listadoPais.html", {'paises' : paisBdd})
#renderizando formulario de nuevo Género
def nuevoPais(request):
    return render(request,'nuevoPais.html')
#Insertando Genero en la base de datos 
def guardarPais(request):
    nom=request.POST["nombre"]
    con=request.POST["continente"]
    cap=request.POST["capital"]
    nuevoPais=Pais.objects.create(nombre=nom, continente=con, capital=cap )
    messages.success(request, "Pais registrado exitosamente")
    return redirect('listadoPais')
#Se recibe el id para eliminar 
def eliminarPais(request,id):
    paisEliminar=Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, "Pais eliminado Correctamente")
    return redirect('/listadoPais') 
#Renderozando formulario de actualización 
def editarPais(request, id):
    paisEditar=Pais.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar':paisEditar})
#Actualizando nuevos datos en la BDD
def procesarActualizacionPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request, 'Pais actualizado exitosamente.')
    return redirect('listadoPais')

#-------------------------------DIRECTORES----------------------------------------------------s
def gestionDirectores(request):
    return render (request ,'gestionDirectores.html')
#crear una nueva variable 
def listadoDirectores(request):
    directorBdd=Director.objects.all()
    return render(request,"listadoDirectores.html", {'directores' : directorBdd})
#renderizando formulario de nuevo Género
def nuevoDirector(request):
    return render(request,'nuevoDirector.html')
#Insertando Genero en la base de datos 
@csrf_exempt
def guardarDirector(request):
    dni=request.POST["dni"]
    apellidos=request.POST["apellidos"]
    nombre=request.POST["nombre"]
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni, apellidos=apellidos, nombre=nombre, foto=fot)
    return JsonResponse({
        'estado': True,
        'mensaje': 'Género registrado exitosamente.',
    })
#Se recibe el id para eliminar 
def eliminarDirector(request,id):
    directorEliminar=Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, "Director eliminado Correctamente")
    return redirect('/listadoDirectores') 
#Renderozando formulario de actualización 
def editarDirector(request, id):
    directorEditar=Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar':directorEditar})
#Actualizando nuevos datos en la BDD
def procesarActualizacionDirector(request):
    id=request.POST['id']
    dni=request.POST['dni']
    apellidos=request.POST['apellidos']
    nombre=request.POST['nombre']
    fot=request.FILES.get("foto")
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.nombre=nombre
    directorConsultado.apellidos=apellidos
    directorConsultado.foto=fot
    directorConsultado.save()
    messages.success(request, 'Director actualizado exitosamente.')
    return redirect('listadoDirectores')
# ------------------------------------------CINE --------------------------
# funcion para gestionar el CRUD de cine 
def gestionCines(request):
    return render (request ,'gestionCines.html')
# guardar cine 
#Insertando cines mediante AJAX en la Base de Datos
@csrf_exempt
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Género registrado exitosamente.',
    })
#renderizar listado cines
def listadoCines(request):
    cineBdd=Cine.objects.all()
    return render(request,"listadoCines.html", {'cines' : cineBdd})
#---------------------------Peliculas--------------------------------------------------
def gestionPelicula(request):
    director = Director.objects.all()
    genero = Genero.objects.all()
    return render(request,'gestionPelicula.html',{'directores':director,'generos':genero})
@csrf_exempt
def guardarPelicula(request):
    tit = request.POST["titulo"]
    dur = request.POST["duracion"]
    sip = request.POST["sinopsis"]

    gen = request.POST["genero"]
    genero_instancia = Genero.objects.get(id=gen)

    dir = request.POST["director"]
    director_instancia = Director.objects.get(id=dir)

    nuevaPelicula = Pelicula.objects.create(
        titulo=tit, duracion=dur, sinopsis=sip,
        genero=genero_instancia, director=director_instancia
    )

    return JsonResponse({
        'estado': True,
        'mensaje': 'Película registrada exitosamente.'
    })
