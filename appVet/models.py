from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='servicios/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)   
    
    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    sucursal = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    puesto = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre