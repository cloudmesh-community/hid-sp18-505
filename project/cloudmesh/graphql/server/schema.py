import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Raingage as RaingageModel


class Raingage(MongoengineObjectType):

    class Meta:
        model = RaingageModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    status = graphene.String()

    node = Node.Field()
    all_raingages = MongoengineConnectionField(Raingage)

    def resolve_status(self, args):
        return 'ok'


schema = graphene.Schema(query=Query, types={Raingage})