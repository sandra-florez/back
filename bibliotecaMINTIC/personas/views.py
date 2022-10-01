import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from . models import *

def index(request):

    return HttpResponse("PERSONAS")

########################################################################
#                       Métodos POST Personas                          #
########################################################################

def agregarCargo(request):
    if request.method == 'POST':
        try:
            dato = json.loads(request.body)

            cargo = cat_cargos(
                cod_cargo = dato["cod_cargo"],
                des_cargo = dato["des_cargo"],
                cod_estado = dato["cod_estado"],
                sw_empleado = dato["sw_empleado"]
            )

            cargo.save()

            return HttpResponse("Agregando Cargo.... \n Cargo agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(["POST"], "Método Invalido")

def agregarEstadoPersona(request):
    if request.method == 'POST':
        try:
            dato = json.loads(request.body)

            estado = cat_estados_per(
                cod_estado_per = dato["cod_estado_per"],
                des_estado_per = dato["des_estado_per"],
                sw_activo = dato["sw_activo"]
            )

            estado.save()

            return HttpResponse("Agregando Estado.... \n Estado agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(["POST"], "Método Invalido")

def agregarPersona(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
           
            lr_personas = cat_personas(
                # cod_persona    = data["cod_persona"],
                tipo_documento = data["tipo_documento"],
                num_documento  = data["num_documento"],
                nombres        = data["nombres"],
                apellidos      = data["apellidos"],
                cod_cargo_id   = data["cod_cargo"],
                direccion      = data["direccion"],
                tel_movil      = data["tel_movil"],
                des_municipio  = data["des_municipio"],
                email          = data["email"],
                fec_nacimiento = data["fec_nacimiento"],
                fec_ingreso    = data["fec_ingreso"],
                # fec_nacimiento = "2020-09-09",
                # fec_ingreso    = "2023-09-09",
                cod_estado_per_id = data["cod_estado_per"]
            )
            print(lr_personas.fec_ingreso)
            
            lr_personas.save()
            
            return HttpResponse("AGREGANDO PERSONA\nPERSONA AGREGADA")
        except:
            return HttpResponseBadRequest("ERROR EN LOS DATOS ENVIADOS")
    else:
        return HttpResponseNotAllowed(['POST'],"METODO INVALIDO")

def agregarAcceso(request):
    if request.method == 'POST':
        try:

            data = json.loads(request.body)
            print("antes de captar")
            print(data)
            accesos = cat_accesos(
                cod_persona_id = data["cod_persona"],
                login = data["login"],
                clave = data["clave"],
                fec_cambio = data["fec_cambio"]
            )
            print("antes de enviar")
            print(accesos.cod_persona_id)
            print(accesos.login)
            print(accesos.clave)
            print(accesos.fec_cambio)

            accesos.save()
            print("despues de enviar")
            return HttpResponse("AGREGANDO ACCESO... \nACCESO AGREGADO")
        except:
            return HttpResponseBadRequest("ERROR EN LOS DATOS ENVIADOS")
    else:
        return HttpResponseNotAllowed(['POST'], "METODO INVALIDO")


########################################################################
#                       Métodos GET Personas                           #
########################################################################

def consultarPersonas(request):
    if (request.method == 'GET'):
        try:
            lr_personas = cat_personas.objects.all()
            allPersonasData = []
            for x in lr_personas:
                data = {
                    "cod_persona":x.cod_persona,
                    "tipo_documento":x.tipo_documento,
                    "num_documento":x.num_documento,
                    "nombres":x.nombres,
                    "apellidos":x.apellidos,
                    "cod_cargo":x.cod_cargo_id,
                    "direccion":x.direccion,
                    "tel_movil":x.tel_movil,
                    "des_municipio":x.des_municipio,
                    "email":x.email,
                    "fec_nacimiento":x.fec_nacimiento.strftime("%Y-%m-%d"),
                    "fec_ingreso":x.fec_ingreso.strftime("%Y-%m-%d"),
                    "cod_estado_per":x.cod_estado_per_id
                }
                
                allPersonasData.append(data)
            infoJson = json.dumps(allPersonasData)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = "text/json"
            respuesta.content = infoJson
            return respuesta
        
        except:
            return HttpResponseBadRequest("Error en retorno de datos")

    else:
            return HttpResponseNotAllowed(['GET'],"METODO INVALIDO")

def consultarPersona(request, NumDocumento):
    if(request.method == "GET"):
        try:
            # personas = cat_personas.objects.filter(num_documento__icontains = NumDocumento)
            personas = cat_personas.objects.filter(num_documento = NumDocumento)
            listPersonas = [];
            for x in personas:
                data = {
                    "cod_persona":x.cod_persona,
                    "tipo_documento":x.tipo_documento,
                    "num_documento":x.num_documento,
                    "nombres":x.nombres,
                    "apellidos":x.apellidos,
                    "cod_cargo":x.cod_cargo_id,
                    "direccion":x.direccion,
                    "tel_movil":x.tel_movil,
                    "des_municipio":x.des_municipio,
                    "email":x.email,
                    "fec_nacimiento":x.fec_nacimiento.strftime("%Y-%m-%d"),
                    "fec_ingreso":x.fec_ingreso.strftime("%Y-%m-%d"),
                    "cod_estado_per":x.cod_estado_per_id
                }
                listPersonas.append(data)
            infoJson = json.dumps(listPersonas)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = "text/json"
            respuesta.content = infoJson
            return respuesta
        except:
            return HttpResponseBadRequest("No existe libro")
    else:
        return HttpResponseNotAllowed(["GET"], "Método invalido")

def consultarCargos(request):
    if (request.method == 'GET'):
        try:
            listaCargos = cat_cargos.objects.all()
            allCargos = []
            for x in listaCargos:
                data = {
                    "cod_cargo":x.cod_cargo,
                    "des_cargo":x.des_cargo,
                    "cod_estado":x.cod_estado,
                    "sw_empleado":x.sw_empleado
                }
                
                allCargos.append(data)
            infoJson = json.dumps(allCargos)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = "text/json"
            respuesta.content = infoJson
            return respuesta
        
        except:
            return HttpResponseBadRequest("Error en retorno de datos")

    else:
            return HttpResponseNotAllowed(['GET'],"METODO INVALIDO")

def consultarCargo(request, codCargo):
    if (request.method == 'GET'):
        try:
            listaCargos = cat_cargos.objects.filter(cod_cargo = codCargo)
            allCargos = []
            for x in listaCargos:
                data = {
                    "cod_cargo":x.cod_cargo,
                    "des_cargo":x.des_cargo,
                    "cod_estado":x.cod_estado,
                    "sw_empleado":x.sw_empleado
                }
                
                allCargos.append(data)
            infoJson = json.dumps(allCargos)
            respuesta = HttpResponse()
            respuesta.headers['Content-Type'] = "text/json"
            respuesta.content = infoJson
            return respuesta
        
        except:
            return HttpResponseBadRequest("Error en retorno de datos")

    else:
            return HttpResponseNotAllowed(['GET'],"METODO INVALIDO")