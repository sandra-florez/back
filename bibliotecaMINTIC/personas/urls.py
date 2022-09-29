from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name ='Personas'),
    path('agregarPersona', views.agregarPersona, name='agregarPersona'),
    
    # Rutas GET Personas
    path('consultarPersona', views.consultarPersona, name='consultarPersona'),

    # POST
    path('agregarCargo', views.agregarCargo, name='agregarCargo'),
    path('agregarEstadoPersona', views.agregarEstadoPersona, name='agregarEstadoPersona'),
    path('agregarAcceso', views.agregarAcceso, name='agregarAcceso')
]
