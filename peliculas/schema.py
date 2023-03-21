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
    
class CreatePelicula(graphene.Mutation):
    id          = graphene.Int()
    nombre      = graphene.String()
    estudio     = graphene.String()
    genero      = graphene.String()
    duracion    = graphene.Int()
    recaudacion = graphene.Float()
    productor   = graphene.String()
    valoracion  = graphene.Int()
    servicio    = graphene.String()

    #2
    class Arguments:
        nombre      = graphene.String()
        estudio     = graphene.String()
        genero      = graphene.String()
        duracion    = graphene.Int()
        recaudacion = graphene.Float()
        productor   = graphene.String()
        valoracion  = graphene.Int()
        servicio    = graphene.String()

    #3
    def mutate(self, info, nombre, estudio, genero, duracion, recaudacion, productor, valoracion, servicio):
        pelicula = Pelicula(nombre=nombre, estudio=estudio, genero=genero, duracion=duracion, 
                    recaudacion=recaudacion, productor=productor, valoracion=valoracion, servicio=servicio)
        pelicula.save()

        return CreatePelicula(
            id=pelicula.id,
            nombre=pelicula.nombre,
            estudio=pelicula.estudio,
            genero=pelicula.genero,
            duracion=pelicula.duracion,
            recaudacion=pelicula.recaudacion,
            productor=pelicula.productor,
            valoracion=pelicula.valoracion,
            servicio=pelicula.servicio
        )

class Mutation(graphene.ObjectType):
    create_peliculas = CreatePelicula.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)