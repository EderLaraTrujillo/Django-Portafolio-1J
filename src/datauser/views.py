from django.shortcuts import render, HttpResponse   # Paquete para Vistas basadas en funciones
from django.views.generic.base import TemplateView  # Paquete para Vistas basadas en clases
# Importamos formularios:
from .forms import DatosUsers

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

def DatosPageView(request):
    template_name = 'datosuser.html'
    formulario = DatosUsers()

    return render(request, template_name, {'formulario':formulario})