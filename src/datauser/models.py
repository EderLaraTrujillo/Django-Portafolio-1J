from django.db import models
from django.db.models.deletion import CASCADE
# Usar foraneas de las tablas de django:
from django.conf import settings

# Create your models here.

class DatosPersonales(models.Model):
    # Atributos de la clase:
    identidy_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, verbose_name="id Usuario")
    telefono_user = models.CharField(verbose_name="Telefono Usuario", max_length = 25, blank=True)
    describe_user = models.TextField(verbose_name="Perfil del Usuario", blank=True)
    linkedind_lnk = models.URLField(verbose_name="Url LinkedIn")

    class Meta:
        verbose_name = "Datos del Usuario"
        verbose_name_plural = "Datos del Perfil"
    
    def __str__(self):
        return f'{self.identidy_user}'