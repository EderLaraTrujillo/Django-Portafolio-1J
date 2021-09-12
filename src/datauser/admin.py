import datauser
from django.contrib import admin

# Register your models here.
from .models import DatosPersonales, Habilidades, Perfil


# Matriculamos el módulo - Modelo:
class DatosPersonalesModel(admin.ModelAdmin):
    list_display = ["telefono_user", "describe_user",]
    list_display_links = ["telefono_user", "describe_user",]
    list_filter = ["telefono_user"]

    class Meta:
        model: DatosPersonales

admin.site.register(DatosPersonales)
admin.site.register(Habilidades)
admin.site.register(Perfil)