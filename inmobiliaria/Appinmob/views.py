from django.http import HttpResponse
from Appinmob.models import *
from django.template import loader
from django.shortcuts import render
from Appinmob.forms import *

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def buscar_propiedad(request):
    return render (request, "buscar_propiedad.html")

#Verificar codigo de busqueda. posee falla aun no encontrada

def buscar_pro(request):
    if request.method == "POST":
        dimensiones= request.POST['dimensiones']
        Propiedades=Propiedad.objects.filter(dimensiones__icontains = dimensiones)
        return render(request, "resultado_busqueda_propiedades.html", {"Propiedades": Propiedades})
    else:
        return render(request, "error.html")

    
    
    return render(request, "formulario_buscar_propiedad.html")


# lo dejo asi para mostrar otra forma de cargar datos y tenerlo sin filtro para futuras pruebas
def alta_propiedad(request):
    if request.method == "POST":
        db= Propiedad(titular=request.POST['titular'], ubicacion=request.POST['ubicacion'], dimensiones=request.POST['dimensiones'], poseecartel=request.POST['poseecartel'])
        db.save()
        return render(request, "formulario_alta_propiedad.html")

    return render (request, "formulario_alta_propiedad.html")
#carga las ventas realizadas en la db
def alta_venta(request):
    if request.method == "POST":
        datos_formulario = Form_venta(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Venta(nombremartillero=midata['nombremartillero'], comprador=midata['comprador'])
            db.save()
        return render(request, "formulario_alta_venta.html")
    return render(request, "formulario_alta_venta.html")

#carga las propiedades alquiladas en una db
def alta_alquiler(request):
    if request.method == "POST":
        datos_formulario = Form_alquiler(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Alquiler(inquilino=midata['inquilino'], dueño=midata['dueño'])
            db.save()
        return render(request, "formulario_alta_alquiler.html")
    return render(request, "formulario_alta_alquiler.html")

#carga nuevos martilleros en la db
def alta_martillero(request):
    if request.method == "POST":
        datos_formulario = Form_martillero(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Martillero(nombre=midata['nombre'], Apellido=midata['Apellido'], dni=midata['dni'])
            db.save()
        return render(request, "formulario_alta_martillero.html")
    return render(request, "formulario_alta_martillero.html")

#carga nuevas consultas en la base de datos
def alta_contacto(request):
    if request.method == "POST":
        datos_formulario = Form_contacto(request.POST)
        if datos_formulario.is_valid():
            midata=datos_formulario.cleaned_data
            db= Contacto(nombre=midata['nombre'], apellido=midata['apellido'], email=midata['email'], telefono=midata['telefono'], mensaje=midata['mensaje'])
            db.save()
        return render(request, "formulario_alta_contacto.html")
    return render(request, "formulario_alta_contacto.html")