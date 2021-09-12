from django.shortcuts import render, HttpResponse   # Paquete para Vistas basadas en funciones
from django.views.generic.base import TemplateView  # Paquete para Vistas basadas en clases

# Create your views here.
# Vistas basadas en clases:
class HomePageView(TemplateView):
    # Atributo que indica que template html debe usar:
    template_name = 'index.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name, {
            'titulo':'Portafolios',
            'mensaje':'Ten acceso a los perfiles, mas solicitados y preparados del momento.',
            'pregunta': '¿Qué esperas para empezar?',
            'boton': 'Registrate!'
        })