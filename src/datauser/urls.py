from django.urls import path
# Importar las vistas:
from .views import HomePageView, LoginPageView, DatosPageView

urlpatterns = [
   path('', HomePageView.as_view(), name='inicio'),
   path('login/', LoginPageView.as_view(), name="ingreso"),
   path('datospersonales/', DatosPageView.as_view(), name="datosuser")
]
