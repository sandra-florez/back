from django.urls import path
from . import views

urlpatterns = [
    #path('', views.libros, name='Libros'),
    # Rutas POST Libros
    path('agregarEditorial', views.agregarEditorial, name='agregarEditorial'),
    path('agregarAutor', views.agregarAutor, name='agregarAutor'),
    path('agregarLibro', views.agregarLibro, name='agregarLibro'),
    path('agregarLibroPlu', views.agregarLibroPlu, name='agregarLibroPlu'),
    # Ruta que agrega Libro completo 
    path('agregarLibroCompleto', views.agregarLibroCompleto, name='agregarLibroCompleto'),
    
    # Rutas GET Libros
    path('consultarLibro/<int:cod_libro>', views.consultarLibro, name='consultarLibro'),
    path('consultarLibroNombre/<str:tit_libro>', views.consultarLibroNombre, name='consultarLibroNombre'),
    path('consultarAutor/<str:des_autor>', views.consultarAutor, name='consultarAutor'),
    path('consultarEditorial/<str:des_editorial>', views.consultarEditorial, name='consultarEditorial'),
    path('consultarLibros', views.consultarLibros, name='consultarLibros'),
]