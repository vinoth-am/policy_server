import graphene
from graphene import ObjectType
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType
from core.models import Insurance


class InsuranceType(DjangoObjectType):
    class Meta:
        model = Insurance
        fields = "__all__"


class CountListType(ObjectType):
    month = graphene.String()
    count = graphene.String()


class InsuranceCountType(ObjectType):
    insurance_count = GenericScalar()
