from django.db import models
from django.utils.timezone import now
from django.conf import settings

class Pelicula(models.Model):
    nombre =      models.TextField(blank=False, default=' ')
    estudio =     models.TextField(blank=False, default=' ')
    genero =      models.TextField(default=' ', blank=False)
    anio =        models.DateField(default=now, blank=True)
    duracion =    models.IntegerField(default=90, blank=False)
    recaudacion = models.FloatField(default=0, blank=False)
    director =    models.TextField(default=' ', blank=False)
    productor =   models.TextField(default=' ', blank=False)
    valoracion =  models.IntegerField(default=0, blank=False)
    servicio =    models.TextField(default='', blank=True)
    posted_by =   models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey('peliculas.Pelicula', null=True, related_name='movies', on_delete=models.CASCADE)    