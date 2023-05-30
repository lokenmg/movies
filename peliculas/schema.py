import graphene
from graphene_django import DjangoObjectType
from peliculas.models import Pelicula, Vote
from graphql import GraphQLError
from django.db.models import Q

from .models import Pelicula
from users.schema import UserType

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class PeliculaType(DjangoObjectType):
    class Meta:
        model = Pelicula
    


class Query(graphene.ObjectType):
    peliculas = graphene.List(PeliculaType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_peliculas(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(nombre__icontains=search) |
                Q(estudio__icontains=search)
            )
            return Pelicula.objects.filter(filter)
        return Pelicula.objects.all()
    
    
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
    
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
    posted_by = graphene.Field(UserType)

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
        user = info.context.user or None
        pelicula = Pelicula(
            nombre=nombre, 
            estudio=estudio, 
            genero=genero, 
            duracion=duracion, 
            recaudacion=recaudacion, 
            productor=productor, 
            valoracion=valoracion, 
            servicio=servicio, 
            posted_by=user,)
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
            servicio=pelicula.servicio,
            posted_by=pelicula.posted_by,
        )
    

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    peli = graphene.Field(PeliculaType)

    class Arguments:
        movie_id = graphene.Int()

    def mutate(self, info, movie_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')

        peli = Pelicula.objects.filter(id=movie_id).first()
        if not peli:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            movie=peli,
        )

        return CreateVote(user=user, peli=peli)

class Mutation(graphene.ObjectType):
    create_peliculas = CreatePelicula.Field()
    create_vote = CreateVote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)