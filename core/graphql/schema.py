import graphene
from core.graphql.query import Query
from core.graphql.mutations import Mutation

schema = graphene.Schema(query=Query,
                         mutation=Mutation
                         )
