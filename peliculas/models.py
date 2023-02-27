from django.db import models
from django.utils.timezone import now
class Pelicula(models.Model):
    nombre = models.TextField(blank=False, default=' ')
    estudio = models.TextField(blank=False, default=' ')
    genero = models.TextField(default=' ', blank=False)
    anio = models.DateField(default=now, blank=True)
    duracion = models.IntegerField(default=90, blank=False)
    recaudacion= models.FloatField(default=0, blank=False)
    director = models.TextField(default=' ', blank=False)
    productor = models.TextField(default=' ', blank=False)
    valoracion = models.IntegerField(default=0, blank=False)
    servicio = models.TextField(default='', blank=True)
        