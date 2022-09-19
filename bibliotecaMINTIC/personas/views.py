import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from . models import personas

def index(request):
    return HttpResponse("PERSONAS")

def agregarPersona(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lr_personas = personas(
                tipo_documento = data["tipo_documento"]
                ,num_documento  = data["num_documento"]
                ,nombres        = data["nombres"]
                ,apellidos      = data["apellidos"]
                ,cod_cargo      = data["cod_cargo"]
                ,direccion      = data["direccion"]
                ,tel_movil      = data["tel_movil"]
                ,des_municipio  = data["des_municipio"]
                ,email          = data["email"]
                ,fec_nacimiento = data["fec_nacimiento"]
                ,cod_estado_per = data["cod_estado_per"]
            )
            lr_personas.save()
            return HttpResponse("AGREGAR PERSONA")
        except:
            return HttpResponseBadRequest("ERROR EN LOS DATOS ENVIADOS")
    else:
        return HttpResponseNotAllowed(['POST'],"METODO INVALIDO")

def consultarPersona(request):
    if request.method == 'GET':
        lr_personas = personas.objects.all()
        allPersonasData = []
        for x in lr_personas:
            data = {"cod_persona":x.cod_persona
                    ,"tipo_documento":x.tipo_documento
                    ,"num_documento":x.num_documento
                    ,"nombres":x.nombres
                    ,"apellidos":x.apellidos
                    ,"cod_cargo":x.cod_cargo
                    ,"direccion":x.direccion
                    ,"tel_movil":x.tel_movil
                    ,"des_municipio":x.des_municipio
                    ,"email":x.email
                    ,"fec_nacimiento":x.fec_nacimiento
                    ,"cod_estado_per":x.cod_estado_per}
            allPersonasData.append(data)
        dataJson = json.dumps(allPersonasData)
        print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-type'] = "text/json"
        resp.content = dataJson
        return HttpResponse(resp)
    else:
        return HttpResponseNotAllowed(['GET'],"METODO INVALIDO")
