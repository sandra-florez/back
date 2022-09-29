from django.db import models


class cat_cargos(models.Model):
    cod_cargo = models.SmallIntegerField(primary_key = True)
    des_cargo = models.CharField(max_length = 45)
    cod_estado = models.CharField(max_length = 3)
    sw_empleado = models.SmallIntegerField()


class cat_estados_per(models.Model):
    cod_estado_per = models.CharField(max_length = 3, primary_key = True)
    des_estado_per = models.CharField(max_length = 45)
    sw_activo = models.SmallIntegerField()

class cat_personas(models.Model):
    cod_persona = models.AutoField(primary_key = True)
    tipo_documento = models.CharField(max_length =3)
    num_documento = models.CharField(max_length =25)
    nombres = models.CharField(max_length = 45)
    apellidos = models.CharField(max_length = 45)
    cod_cargo = models.ForeignKey(cat_cargos, related_name="codigoCargo", on_delete = models.CASCADE, default = 20)
    direccion = models.CharField(max_length = 45)
    tel_movil = models.PositiveIntegerField()
    des_municipio = models.CharField(max_length = 55)
    email = models.EmailField()
    fec_nacimiento = models.DateField()
    fec_ingreso = models.DateField()
    cod_estado_per = models.ForeignKey(cat_estados_per, related_name="codigoEstadoPersona", on_delete = models.RESTRICT,default='NOR')


class cat_accesos(models.Model):
    cod_persona = models.ForeignKey(cat_personas, related_name = "codigoPersona", on_delete = models.CASCADE, default = 16)
    login = models.CharField(max_length = 25)
    clave = models.CharField(max_length = 255)
    fec_cambio = models.DateField()
