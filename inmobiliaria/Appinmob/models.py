from django.db import models

# Create your models here.

class Propiedad(models.Model):
    titular = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)
    dimensiones = models.CharField(max_length=30)
    poseecartel = models.BooleanField()


class Martillero(models.Model):
    nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    dni = models.IntegerField()

class Venta(models.Model):
    nombremartillero = models.CharField(max_length=40)
    comprador = models.CharField(max_length=40)

class Alquiler(models.Model):
    inquilino = models.CharField(max_length=40)
    dueño = models.CharField(max_length=40)

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length = 254)
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=100)

