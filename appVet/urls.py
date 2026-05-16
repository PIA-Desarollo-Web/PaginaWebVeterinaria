from django.urls import path
from . import views

urlpatterns = [
    path('' , views.inicio,name="inicio"), 
    path('agendar' , views.agendarCita,name="inicio"), 
    path('nosotros' , views.nosotros,name="inicio"), 
    path('servicios' , views.servicios,name="inicio"), 
    path('sucursales' , views.sucursales,name="inicio")
]
