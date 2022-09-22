from django.db import models

class Citas(models.Model):
    Tatuador = models.CharField(max_length=100, blank=False, default='')
    Fecha = models.DateField()
    Hora = models.TimeField()
    Imagen = models.ImageField()
    Descripcion = models.CharField(max_length=250, blank=False, default='')


class Publicacion(models.Model):
    imagen=models.ImageField()
    descripcion=models.TextField(max_length=200)
    tatuador=models.CharField(max_length=50)
    fecha_publicacion=models.DateField()


class RegistroUsuarios (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.TextField()
    fecha_nacimiento = models.DateField()
    ciudad = models.TextField()
    departamento = models.TextField()
    direccion = models.TextField()
    email = models.TextField()

class RegistroTatuadores (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.TextField()
    fecha_nacimiento = models.DateField()
    ciudad = models.TextField()
    departamento = models.TextField()
    email = models.TextField()
    experiencia = models.CharField(max_length=4)
