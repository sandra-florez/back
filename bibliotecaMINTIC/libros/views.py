from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotAllowed

def principal(request):
    return HttpResponse("Aquí va la vista principal de Libros!")

def agregarLibro(request):
    if (request.method == "POST"):
        return HttpResponse("Agregando Libro...")
    elif(request.method == "GET"):
        return HttpResponse("Aquí se agrega un Libro!")
    else:
        return HttpResponseNotAllowed(["POST","GET"], "Método invalido")

def consultarLibro(request):
    return HttpResponse("Aquí se consulta un libro!")

def consultarLibros(request):
    return HttpResponse("Aquí se consultan varios libros!")