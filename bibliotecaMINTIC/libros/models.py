from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class cat_editoriales(models.Model):
    cod_editorial = models.IntegerField(primary_key=True)
    des_editorial = models.CharField(max_length=255)


class cat_autores(models.Model):
    cod_autor = models.IntegerField(primary_key=True)
    des_autor = models.CharField(max_length=255)


class cat_libros(models.Model):
    cod_libro = models.IntegerField(primary_key=True)
    tit_libro = models.CharField(max_length=255)
    cod_autor = models.ForeignKey(cat_autores, on_delete=models.CASCADE, related_name="codigoAutor" )
    cod_editorial = models.ForeignKey(cat_editoriales, related_name="codigoEditorial", on_delete=models.CASCADE)
    anio = models.SmallIntegerField()
    tema = models.CharField(max_length=255)
    cant_plu = models.SmallIntegerField()
    cant_disponible = models.SmallIntegerField()

class cat_libros_plu(models.Model):
    cod_libro = models.ForeignKey(cat_libros, related_name="codigoLibro", on_delete=models.RESTRICT)
    plu = models.CharField(max_length=25, primary_key=True)
    cant_disponible = models.SmallIntegerField()