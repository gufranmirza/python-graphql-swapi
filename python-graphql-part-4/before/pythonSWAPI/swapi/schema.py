import graphene

from swapi.types import HumanType
from swapi.models import Human 
from swapi.resolvers import resolver_human, resolver_humans

class Query(graphene.ObjectType):
    hello = graphene.String()
    def resolve_hello(self, info, **kwargs):
        return "world"

    humans = graphene.List(HumanType)
    def resolve_humans(self, info):
        return resolver_humans()

    human = graphene.Field(
        HumanType, 
        id=graphene.NonNull(graphene.Int)
    )
    def resolve_human(self, info, id):
        return resolver_human(id=id)

schema = graphene.Schema(query=Query)