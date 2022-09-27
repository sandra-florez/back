from django.shortcuts import render
import json

# Create your views here.

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .models import *

########################################################################
#                       Vista Principal Libros                         #
########################################################################
def libros(request):
    if(request.method == "GET"):        
        try:
            return HttpResponse("Aquí va la vista principal de Libros!")
        except:
            return HttpResponseBadRequest(["GET"], "Error en retorno de datos")
    else:        
        return HttpResponseNotAllowed(["GET"], "Método invalido")

########################################################################
#                       Métodos POST Libros                            #
########################################################################

def agregarLibroCompleto(request):
    if (request.method == "POST"):
        try:
            dato = json.loads(request.body)
            print(dato)
            
            
            autor = cat_autores(
                cod_autor = dato["cod_autor"],
                des_autor = dato["des_autor"]
            )
            #Validar si autos-editorial ya existen.
            autor.save()


            print("AUTORES")

            editorial = cat_editoriales(
                cod_editorial = dato["cod_editorial"],
                des_editorial = dato["des_editorial"]
            )
            editorial.save()

            print("EDITORIAL")

            libros = cat_libros(
                cod_libro = dato["cod_libro"],
                tit_libro = dato["tit_libro"],
                cod_autor_id = dato["cod_autor"],
                cod_editorial_id = dato["cod_editorial"],
                anio = dato["anio"],
                tema = dato["tema"],
                cant_plu = dato["cant_plu"],
                cant_disponible = dato["cant_disponible"]
            )
            print("LIBRO ANTES DE GUARDAR")
            libros.save()

            print("LIBRO DESPUES DE GUARDADO")

            libros_plu = cat_libros_plu(
                cod_libro_id = dato["cod_libro"],
                plu = dato["plu"],
                cant_disponible = dato["cant_disponible_plu"]
            )
            libros_plu.save()

            print("PLU")
            #esta respuesta la recoge data en el js.
            return HttpResponse("Agregando Libro Completo... \nLibro Completo agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(["POST"], "Método invalido")

def agregarEditorial(request):
    if (request.method == "POST"):
        try:
            dato = json.loads(request.body)

            editorial = cat_editoriales(
                cod_editorial = dato["cod_editorial"],
                des_editorial = dato["des_editorial"]
            )
            editorial.save()

            return HttpResponse("Agregando Editorial... \nEditorial agregada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(["POST"], "Método invalido")

def agregarAutor(request):
    if (request.method == "POST"):
        try:
            dato = json.loads(request.body)
            print(dato);

            autor = cat_autores(
                cod_autor = dato["cod_autor"],
                des_autor = dato["des_autor"]
            )
            autor.save()

            return HttpResponse("Agregando Autor... \nAutor agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(["POST"], "Método invalido")

def agregarLibro(request):
    if (request.method == "POST"):
        try:
            dato = json.loads(request.body)
            print(dato);

            libros = cat_libros(
                cod_libro = dato["cod_libro"],
                tit_libro = dato["tit_libro"],
                cod_autor_id = dato["cod_autor"],
                cod_editorial_id = dato["cod_editorial"],
                anio = dato["anio"],
                tema = dato["tema"],
                cant_plu = dato["cant_plu"],
                cant_disponible = dato["cant_disponible"]
            )
            libros.save()

            return HttpResponse("Agregando Libro... \nLibro agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(["POST"], "Método invalido")

def agregarLibroPlu(request):
    if (request.method == "POST"):
        try:
            dato = json.loads(request.body)

            libros_plu = cat_libros_plu(
                cod_libro_id = dato["cod_libro"],
                plu = dato["plu"],
                cant_disponible = dato["cant_disponible_plu"]
            )
            libros_plu.save()

            return HttpResponse("Agregando LibroPlu... \nLibroPlu agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(["POST"], "Método invalido")

########################################################################
#                       Métodos GET Libro                              #
########################################################################
def consultarLibro(request,cod_libro):
    if (request.method == "GET"):
        try:
            libro = cat_libros.objects.filter(cod_libro = cod_libro).first()
            editorial = cat_editoriales.objects.filter(cod_editorial = libro.cod_editorial_id).first()
            autor = cat_autores.objects.filter(cod_autor = libro.cod_autor_id).first()
            datos = {
                "cod_libro": libro.cod_libro,
                "tit_libro": libro.tit_libro,
                "cod_autor_id": libro.cod_autor_id,
                "cod_editorial_id": libro.cod_editorial_id,
                "anio": libro.anio,
                "tema": libro.tema,
                "cant_plu": libro.cant_plu,
                "cant_disponible": libro.cant_disponible,
                "des_editorial": editorial.des_editorial,
                "des_autor": autor.des_autor
            }
            datosJson = json.dumps(datos)
            respuesta=HttpResponse()
            respuesta.headers['Content-Type'] = "text/json"
            respuesta.content = datosJson
            return respuesta
        except:
            return HttpResponseBadRequest("Error en retorno de datos")
    else:
        return HttpResponseNotAllowed(["GET"], "Método invalido")

########################################################################
#                       Métodos GET Libros                             #
########################################################################

def consultarLibros(request):
    if (request.method == "GET"):
        try:
            libros = cat_libros.objects.all()
            listaLibros=[]
            for libro in libros:

                editorial = cat_editoriales.objects.filter(cod_editorial = libro.cod_editorial_id).first()
                autor = cat_autores.objects.filter(cod_autor = libro.cod_autor_id).first()

                datos = {
                    "cod_libro": libro.cod_libro,
                    "tit_libro": libro.tit_libro,
                    "cod_autor_id": libro.cod_autor_id,
                    "cod_editorial_id": libro.cod_editorial_id,
                    "anio": libro.anio,
                    "tema": libro.tema,
                    "cant_plu": libro.cant_plu,
                    "cant_disponible": libro.cant_disponible,
                    "des_editorial": editorial.des_editorial,
                    "des_autor": autor.des_autor
                }

                listaLibros.append(datos)
            infoJson = json.dumps(listaLibros)
            
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = "text/json"
            respuesta.content = infoJson
            return respuesta
        except:
            return HttpResponseBadRequest("Error en retorno de datos")

    else:
        return HttpResponseNotAllowed(["GET"], "Método invalido")