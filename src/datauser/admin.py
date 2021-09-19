import datauser
from django.contrib import admin

# Register your models here.
from .models import DatosPersonales, Habilidades


# Matriculamos el módulo - Modelo:
class DatosPersonalesModel(admin.ModelAdmin):
    date_hierarchy = 'modificado_el'
    list_display = ["identidy_user","telefono_user", "describe_user","linkedind_lnk"]
    list_display_links = ["identidy_user", "telefono_user", "describe_user",]
    list_filter = ["identidy_user"]
    readonly_fields = ('creado_el', 'modificado_el')
    search_fields = ("identidy_user","telefono_user", "describe_user","linkedind_lnk")
    

    class Meta:
        model: DatosPersonales

admin.site.register(DatosPersonales, DatosPersonalesModel)
admin.site.register(Habilidades)
