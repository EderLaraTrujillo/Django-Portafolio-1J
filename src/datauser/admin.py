import datauser
from django.contrib import admin

# Register your models here.
from .models import DatosPersonales


# Matriculamos el módulo - Modelo:
admin.site.register(DatosPersonales)