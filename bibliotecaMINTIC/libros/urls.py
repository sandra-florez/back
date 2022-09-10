from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='Libros'),
    path('agregarLibro', views.agregarLibro, name='agregarLibro'),
    path('consultarLibro', views.consultarLibro, name='consultarLibro'),
    path('consultarLibros', views.consultarLibros, name='consultarLibros'),
]
