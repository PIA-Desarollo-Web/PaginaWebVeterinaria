from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def agendarCita(request):
    return render(request, "agendarCita.html")

def nosotros(request):
    return render(request, "nosotros.html")

def servicios(request):
    return render(request, "servicios.html")

def sucursales(request):
    return render(request, "sucursales.html")