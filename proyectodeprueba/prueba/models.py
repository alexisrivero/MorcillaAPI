from django.db import models

# Create your models here.


class Pizza(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    fecha_creacion = models.DateField()

    def __str__(self):
        return 'Pizza:' + self.nombre


class Cocinero(models.Model):
    nombre = models.CharField(max_length=200)
    nacionalidad = models.ForeignKey(
        'Pais', on_delete=models.DO_NOTHING, blank=True, null=True)
    pizzas = models.ManyToManyField(Pizza)

    def __str__(self):
        return 'Cocinero:' + self.nombre


class Pais(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Paises'

    def __str__(self):
        return 'Pais:' + self.nombre
