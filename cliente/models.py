from django.db import models

# Create your models here.


class Cliente(models.Model):

    ci = models.CharField(max_length=20,primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=25)
    Genero = (
        ('1','Masculino'),
        ('2','Femenino'),
    )
    genero = models.CharField(max_length=1, choices=Genero)

    def __str__(self):
        return self.ci

