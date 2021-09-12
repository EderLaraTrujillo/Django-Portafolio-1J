from django.db import models
from django.db.models.deletion import CASCADE
# Usar foraneas de las tablas de django:
from django.conf import settings

# Create your models here.

class DatosPersonales(models.Model):
    # Atributos de la clase:
    identidy_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, verbose_name="NickName")
    telefono_user = models.CharField(verbose_name="Telefono Usuario", max_length = 25, blank=True)
    describe_user = models.TextField(verbose_name="Perfil del Usuario", blank=True)
    linkedind_lnk = models.URLField(verbose_name="Url LinkedIn")
    creado_el = models.DateTimeField(verbose_name="Creado el", auto_now=True)
    modificado_el = models.DateTimeField(verbose_name="Modificado el", auto_now_add=True)

    class Meta:
        verbose_name = "Datos del Usuario"
        verbose_name_plural = "Datos Personales"
    
    def __str__(self):
        return f'{self.identidy_user}'

class Habilidades(models.Model):
    # atributos de la clase:
    identidy_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = CASCADE, verbose_name= "NickName")
    nombre_habilidad = models.CharField(verbose_name = "Habilidad", max_length = 100)
    porcen_habilidad = models.DecimalField(max_digits = 3, decimal_places = 1, verbose_name= "Porcentaje de Habilidad")
    status_habilidad = models.BooleanField(verbose_name= "Estado de Habilidad", default = True)
    creado_el = models.DateTimeField(verbose_name="Creado el", auto_now=True)
    modificado_el = models.DateTimeField(verbose_name="Modificado el", auto_now_add=True)

    class Meta:
        verbose_name = "Habilidad del Usuario"
        verbose_name_plural = "Habilidades del Usuario"

    def __str__(self) -> str:
        return self.nombre_habilidad

class Servicios(models.Model):
    pass

    

