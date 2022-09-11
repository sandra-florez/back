from django.shortcuts import render
import json

# Create your views here.

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from .models import *

def principal(request):
    return HttpResponse("Aquí va la vista principal de Libros!")

def agregarLibro(request):
    if (request.method == "POST"):
        try:
            dato = json.loads(request.body)
            print(dato)
            
            autor = cat_autores(
                cod_autor = dato["cod_autor"],
                des_autor = dato["des_autor"]
            )
            autor.save()

            print("AUTORES")

            editorial = cat_editoriales(
                cod_editorial = dato["cod_editorial"],
                des_editorial = dato["des_editorial"]
            )
            editorial.save()

            print("EDITORIAL")

            # libros = cat_libros(
            #     cod_libro = dato["cod_libro"],
            #     tit_libro = dato["tit_libro"],
            #     cod_autor_id = dato["cod_autor"],
            #     cod_editorial_id = dato["cod_editorial"],
            #     anio = dato["anio"],
            #     tema = dato["tema"],
            #     cant_plu = dato["cant_plu"],
            #     cant_disponible = dato["cant_disponible_libros"]
            # )
            # libros.save()

            # print("LIBROS")

            # libros_plu = cat_libros_plu(
            #     cod_libro = dato["cod_libro"],
            #     plu = dato["plu"],
            #     cant_disponible = dato["cant_disponible_plu"]
            # )
            # libros_plu.save()

            # print("PLU")

            return HttpResponse("Agregando Libro... \nLibro agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(["POST"], "Método invalido")

def consultarLibro(request):
    if (request.method == "GET"):
        return HttpResponse("Aquí se consulta un libro!")
    else:
        return HttpResponseNotAllowed(["GET"], "Método invalido")

def consultarLibros(request):
    if (request.method == "GET"):
        autores = cat_autores.objects.all()
        listaAutores=[]
        for x in autores:
            dato = {"cod_autor": x.cod_autor, "des_autor": x.des_autor}
            listaAutores.append(dato)
        infoJson = json.dumps(listaAutores);
        
        respuesta = HttpResponse()
        respuesta.headers['Content-Type'] = "text/json"
        respuesta.content = infoJson
        # print(infoJson)
        print("Aquí se consultan varios libros!")
        return respuesta

    else:
        return HttpResponseNotAllowed(["GET"], "Método invalido")