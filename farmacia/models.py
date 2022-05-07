from django.db import models

# Create your models here.

class Medicamento(models.Model):
    codigo = models.AutoField(primary_key=True)	
    descripcion	= models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    contenido = models.PositiveSmallIntegerField()
    gramaje	= models.PositiveSmallIntegerField()
    precio = models.PositiveSmallIntegerField()
    cantidad = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0}, {1} Comprimidos,  {2}mg , ${3}"
        return texto.format(self.descripcion, self.contenido, self.gramaje, self.precio)

class Medico(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        texto = "{0} , {1}"
        return texto.format(self.rut, self.nombre)
