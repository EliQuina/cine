from django.db import models

# Creando modelo Genero : terror, comedia 
class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150,default='')
    foto=models.FileField(upload_to='generos', null=True, blank=True)
    def __str__(self):
        fila="{0}: {1} - {2}"
        return fila.format(self.id,self.nombre,self.descripcion)
    

class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    apellidos=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)
    foto=models.FileField(upload_to='directores', null=True, blank=True)
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id,self.dni,self.apellidos,self.nombre, self.estado)

class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    continente=models.CharField(max_length=15)
    capital=models.CharField(max_length=50) 
    def __str__(self):
        fila="{0}: {1} - {2} - {3} "
        return fila.format(self.id,self.nombre,self.continente,self.capital)

class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField()
    sinopsis=models.TextField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE)
    director=models.ForeignKey(Director, on_delete=models.CASCADE)
    #portada=models.FileField(upload_to='OJO', null=True, blank=True)
    def __str__(self):
        fila="{0}: {1}"
        return fila.format(self.id, self.titulo,self.duracion,self.sinopsis,self.genero,self.director)
    
# Modelo cine 
class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    direccion=models.CharField(max_length=150,default='')
    telefono=models.CharField(max_length=150,default='')
    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id,self.nombre,self.direccion, self.telefono)