from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path("propiedades", views.propiedades),
    path("martilleros", views.martilleros),
    path("ventas", views.ventas),
    path("alquileres", views.alquileres),
    path("contacto", views.contacto),
]