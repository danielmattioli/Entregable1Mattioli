from pyexpat import model
from django.db import models
from django.forms import BooleanField, CharField, EmailField, IntegerField

# Create your models here.

class Propiedad(models.Model):
    titular = CharField(max_length=40)
    ubicacion = CharField(max_length=40)
    dimensiones = CharField(max_length=30)
    poseecartel = BooleanField()


class Martillero(models.Model):
    nombre = CharField(max_length=40)
    Apellido = CharField(max_length=40)
    dni = IntegerField()

class Venta(models.Model):
    nombremartillero = CharField(max_length=40)
    comprador = CharField(max_length=40)

class Alquiler(models.Model):
    inquilino = CharField(max_length=40)
    dueño = CharField(max_length=40)

class Contacto(models.Model):
    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    email = EmailField(max_length = 254)
    telefono = IntegerField()
    mensaje = CharField(max_length=100)

