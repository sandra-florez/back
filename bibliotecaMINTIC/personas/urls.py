from django.urls import path
from . import views 

urlpatterns = [
    path('agregarPersona', views.agregarPersona, name='agregarPersona'),
    
    # Rutas GET Personas
    path('consultarPersona', views.consultarPersona, name='consultarPersona'),
]
