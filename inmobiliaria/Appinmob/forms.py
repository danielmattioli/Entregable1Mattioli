from django import forms

class Form_propiedad(forms.Form):
    titular = forms.CharField(max_length=40)
    ubicacion = forms.CharField(max_length=40)
    dimensiones = forms.CharField(max_length=30)
    poseecartel = forms.CharField(max_length=2)

class Form_venta(forms.Form):
    nombremartillero = forms.CharField(max_length=40)
    comprador = forms.CharField(max_length=40)

class Form_martillero(forms.Form):
    nombre = forms.CharField(max_length=40)
    Apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()

class Form_alquiler(forms.Form):
    inquilino = forms.CharField(max_length=40)
    dueño = forms.CharField(max_length=40)

class Form_contacto(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField(max_length = 254)
    telefono = forms.IntegerField()
    mensaje = forms.CharField(max_length=100)