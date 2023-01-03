from django.db import models

# Create your models here.
class Elemento(models.Model):
    ID=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    calorias=models.PositiveIntegerField()
    peso=models.PositiveIntegerField()
    gain=models.FloatField(default="0")   

    def __str__(self) -> str:
        texto="{0}"
        return texto.format(self.nombre)

    

class SelElemento(models.Model):
    ID=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    calorias=models.PositiveIntegerField()
    peso=models.PositiveIntegerField()
    gain=models.FloatField(default="0")   

    def __str__(self) -> str:
        texto="{0}"
        return texto.format(self.nombre)

class req(models.Model):
    reqcalorias=models.PositiveIntegerField(editable=False)
    reqpeso=models.PositiveIntegerField(editable=False)


