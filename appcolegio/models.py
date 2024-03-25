from django.db import models
from django.conf import Settings

class curso(models.Model):
    nombre = models.CharField(max_length=40)
    division = models.IntegerField()

    def __str__(self):
        return f"curso:{self.nombre} | division:{self.division}"

class estu(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    dni= models.IntegerField()
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"nombre:{self.nombre} | apellido:{self.apellido} | dni:{self.dni} "


class prof(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    dni= models.IntegerField()
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"nombre:{self.nombre} | apellido:{self.apellido} | dni:{self.dni} "

class mate(models.Model):
    nombre = models.CharField(max_length=30)
    codigo= models.IntegerField()

    def __str__(self):
        return f"nombre:{self.nombre} | codigo:{self.codigo} "