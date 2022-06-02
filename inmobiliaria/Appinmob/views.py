from django.http import HttpResponse
from Appinmob.models import *
from django.template import loader
from django.shortcuts import render
from Appinmob.forms import *

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def consulta_propiedades(request):
    return render(request, "formulario_consultas.html")

def buscartitular(request):
    db = Propiedad.objects.all()
    datos ={"datos": db}
    return render(request, "muestraconsulta.html", datos)

def alta_propiedad(request):
    if request.method == "POST":
        db= Propiedad(titular=request.POST['titular'], ubicacion=request.POST['ubicacion'], dimensiones=request.POST['dimensiones'], poseecartel=request.POST['poseecartel'])
        db.save()
        return render(request, "formulario_alta_propiedad.html")

    return render (request, "formulario_alta_propiedad.html")

def alta_venta(request):
    if request.method == "POST":
        datos_formulario = Form_venta(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Venta(nombremartillero=midata['nombremartillero'], comprador=midata['comprador'])
            db.save()
        return render(request, "formulario_alta_venta.html")
    return render(request, "formulario_alta_venta.html")

def alta_alquiler(request):
    if request.method == "POST":
        datos_formulario = Form_alquiler(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Alquiler(inquilino=midata['inquilino'], dueño=midata['dueño'])
            db.save()
        return render(request, "formulario_alta_alquiler.html")
    return render(request, "formulario_alta_alquiler.html")

def alta_martillero(request):
    if request.method == "POST":
        datos_formulario = Form_martillero(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Martillero(nombre=midata['nombre'], Apellido=midata['Apellido'], dni=midata['dni'])
            db.save()
        return render(request, "formulario_alta_martillero.html")
    return render(request, "formulario_alta_martillero.html")

def alta_contacto(request):
    if request.method == "POST":
        datos_formulario = Form_contacto(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Contacto(nombre=midata['nombre'], apellido=midata['apellido'], email=midata['email'], telefono=midata['telefono'], mensaje=midata['mensaje'])
            db.save()
        return render(request, "formulario_alta_contacto.html")
    return render(request, "formulario_alta_contacto.html")