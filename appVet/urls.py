from django.urls import path
from . import views

urlpatterns = [
    path('' , views.inicio,name="inicio"), 
    path('agendar' , views.agendarCita,name="agendar"), 
    path('nosotros' , views.nosotros,name="nosotros"), 
    path('servicios' , views.servicios,name="servicios"), 
    path('sucursales' , views.sucursales,name="sucursales")
]
