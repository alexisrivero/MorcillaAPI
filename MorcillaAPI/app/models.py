from django.db import models

# Create your models here.


class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    ciudades = models.ManyToManyField('Ciudad')
    CUIT = models.CharField(max_length=200)
    cantidad_empleados = models.IntegerField()
    logo = models.ImageField(upload_to="logos/", blank=True)

    def __str__(self):
        return self.nombre


class Telefono(models.Model):
    numero = models.CharField(max_length=200)

    def __str__(self):
        return self.numero
