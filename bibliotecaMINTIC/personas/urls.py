from django.urls import path
from . import views 

urlpatterns = [
    # Principal
    path('', views.index, name ='Personas'),
    
    # Rutas GET Personas
    path('consultarPersonas', views.consultarPersonas, name='consultarPersonas'),
    path('consultarPersona/<str:NumDocumento>', views.consultarPersona, name='consultarPersona'),
    
    path('consultarCargos', views.consultarCargos, name='consultarCargos'),
    path('consultarCargo/<int:codCargo>', views.consultarCargo, name='consultarCargo'),
    path('existeUsuario/<str:tipoDocumento>/<str:numDocumento>', views.existeUsuario, name='existeUsuario'),
    # POST
    path('agregarPersona', views.agregarPersona, name='agregarPersona'),
    path('agregarCargo', views.agregarCargo, name='agregarCargo'),
    path('agregarEstadoPersona', views.agregarEstadoPersona, name='agregarEstadoPersona'),
    path('agregarAcceso', views.agregarAcceso, name='agregarAcceso'),

    # PUT
    path('modificarCargo/<int:codCargo>', views.modificarCargo, name='modificarCargo'),
    # DELETE
    path('eliminarCargo/<int:codCargo>', views.eliminarCargo, name='eliminarCargo'),
]
