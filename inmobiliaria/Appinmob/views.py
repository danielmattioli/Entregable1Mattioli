from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def propiedades(request):
    return render(request, "propiedades.html")

def ventas(request):
    return render(request, "ventas.html")

def alquileres(request):
    return render(request, "alquileres.html")

def martilleros(request):
    return render(request, "martilleros.html")

def contacto(request):
    return render(request, "contacto.html")



