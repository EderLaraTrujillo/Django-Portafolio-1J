from django.shortcuts import render, HttpResponse   # Paquete para Vistas basadas en funciones
from django.views.generic.base import TemplateView  # Paquete para Vistas basadas en clases

# Importamos los modelos:
from .models import DatosPersonales, Habilidades # Eliminamos la tabla Perfil

# Importamos formularios:
from .forms import DatosUsers
from ckeditor.widgets import CKEditorWidget

# Create your views here.
# Vistas basadas en clases:
class HomePageView(TemplateView):
    # Atributo que indica que template html debe usar:
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
                    'titulo':'Portafolios',
                    'mensaje':'Ten acceso a los perfiles, mas solicitados y preparados del momento.',
                    'pregunta': '¿Qué esperas para empezar?',
                    'boton': 'Registrate!'
                })

# Vista para el inicio de sesion:
class LoginPageView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class DatosPageView(TemplateView):
    formulario = DatosUsers()
    template_name = 'datosuser.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'formulario': self.formulario})