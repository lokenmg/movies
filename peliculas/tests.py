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

CREATE_PELICULA_MUTATION='''
  mutation createLinkMutation(
    $nombre:      String, 
    $duracion:    Int, 
    $estudio:     String, 
    $genero:      String, 
    $productor:   String, 
    $recaudacion: Float, 
    $servicio:    String, 
    $valoracion:  Int 
    ){
      createPeliculas(
      duracion:    $duracion,
      estudio:     $estudio,
      genero:      $genero,
      nombre:      $nombre,
      productor:   $productor,
      recaudacion: $recaudacion,
      servicio:    $servicio,
      valoracion:  $valoracion
  ){
    nombre
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



    def test_createPelicula_mutation(self):
        response = self.query(
            CREATE_PELICULA_MUTATION,
            variables={'nombre': 'interestelar', 
                       'duracion': 99, 
                       'estudio': 'Warner Bros',
                       'genero': 'ficcion',
                       'productor': 'Christopher Nolan, Lynda Obst, Emma Thomas',
                       'recaudacion': 100.4,
                       'servicio': 'Netflix',
                       'valoracion': 80
                       }
        )
        print('mutation')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createPeliculas": {"nombre": "interestelar"}}, content['data'])