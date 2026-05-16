from django.contrib import admin
from .models import Doctor, Servicio, Producto, Sucursal, Empleado
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Servicio)
admin.site.register(Producto)
admin.site.register(Sucursal)
admin.site.register(Empleado)