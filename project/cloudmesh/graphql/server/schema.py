import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Raingage as RaingageModel
from services import github_issue_count, REPOSITORIES

class Raingage(MongoengineObjectType):

    class Meta:
        model = RaingageModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    status = graphene.String()
    github_issue_count = graphene.String()

    node = Node.Field()
    all_raingages = MongoengineConnectionField(Raingage)

    def resolve_status(self, args):
        return 'ok'

    def resolve_github_issue_count(self, args):
        print(args)
        repo = github_issue_count(REPOSITORIES[0])
        return(repo)

schema = graphene.Schema(query=Query, types={Raingage})