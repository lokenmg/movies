import graphene

import peliculas.schema


class Query(peliculas.schema.Query, graphene.ObjectType):
    pass

class Mutation(peliculas.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)