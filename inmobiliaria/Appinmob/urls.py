from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = "inicio"),
    #path("buscar_propiedad", views.buscar_propiedad, name = "formulario_buscar_propiedad"),
    #path("buscar_pro",views.buscar_pro),
    path("alta_propiedad", views.alta_propiedad, name = "formulario_alta_propiedad"),
    path("alta_venta", views.alta_venta, name= "formulario_alta_venta"),
    path("alta_alquiler", views.alta_alquiler, name= "formulario_alta_alquiler"),
    path("alta_martillero", views.alta_martillero, name = "formulario_alta_martillero"),
    path("alta_contacto", views.alta_contacto, name = "formulario_alta_contacto"),
]