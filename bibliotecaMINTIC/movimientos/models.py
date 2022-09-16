from django.db import models
# from bibliotecaMINTIC.libros.models import cat_libros_plu
# from bibliotecaMINTIC.personas.models import cat_personas


# Create your models here.
class mov_enc_recibos(models.Model):
    cod_recibo = models.DecimalField(primary_key=True,max_digits=13, decimal_places=0)
    cod_persona = models.ForeignKey('personas.cat_personas', related_name = "codigoPersonaMov", on_delete=models.RESTRICT)
    fec_recibo = models.DateField()
    cant_recibo = models.SmallIntegerField()
    cant_pendiente = models.SmallIntegerField()

class mov_det_recibos(models.Model):
    cod_recibo = models.ForeignKey(mov_enc_recibos, related_name="codigoRecibo", on_delete=models.RESTRICT)
    plu =models.ForeignKey('libros.cat_libros_plu', related_name="Plus", on_delete=models.RESTRICT)
    fec_entrega = models.DateField()
    cant_recibo = models.SmallIntegerField()
    cant_pendiente = models.SmallIntegerField()