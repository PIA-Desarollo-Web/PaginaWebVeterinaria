from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicio, Producto, Doctor
# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def agendarCita(request):
    return render(request, "agendarCita.html")

def nosotros(request):
    doctores = Doctor.objects.all()
    return render(request, "nosotros.html", {
        'doctores': doctores
    })

def servicios(request):
    servicios = Servicio.objects.all()      
    productos = Producto.objects.all()      
    return render(request, "servicios.html", {
        'servicios': servicios,
        'productos': productos
    })

def sucursales(request):
    return render(request, "sucursales.html")