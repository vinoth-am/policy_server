import graphene
from core import models
from core.graphql.resolvers import SearchListResolver, ListResolver
from core.graphql.types import InsuranceType, InsuranceCountType


class Query(graphene.ObjectType):
    search_insurance = graphene.List(InsuranceType,
                                     search=graphene.String(required=True),
                                     resolver=SearchListResolver(models.Insurance))
    chart_data = graphene.Field(InsuranceCountType,
                                region=graphene.String(),
                                resolver=ListResolver(models.Insurance))
