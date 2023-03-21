from django.test import TestCase

from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from movies.schema import schema
from peliculas.models import Pelicula

movies_QUERY = '''
 {
   peliculas {
     id
     nombre
     estudio 
     genero 
     anio
     duracion
     recaudacion
     director 
     productor
     valoracion
     servicio
   }
 }
'''

class MoviesTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.auto1=mixer.blend(Pelicula)
        self.auto2=mixer.blend(Pelicula)

    def test_peliculas_query(self):
        response = self.query(
            movies_QUERY,
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        print("query autos results")
        print(content)
        assert len(content['data']['peliculas']) ==2