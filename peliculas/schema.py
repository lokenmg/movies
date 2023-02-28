import graphene
from graphene_django import DjangoObjectType

from .models import Pelicula


class PeliculaType(DjangoObjectType):
    class Meta:
        model = Pelicula


class Query(graphene.ObjectType):
    peliculas = graphene.List(PeliculaType)

    def resolve_peliculas(self, info, **kwargs):
        return Pelicula.objects.all()