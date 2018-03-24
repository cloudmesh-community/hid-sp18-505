# File: app.py
from flask import Flask
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView
from mongoengine import *
from graphene_mongo import MongoengineObjectType, MongoengineConnectionField
import graphene
from graphene.relay import Node

# See ref: 3
connection = connect('mongoenginetest', host='mongomock://localhost')

# See ref: 3
class TestObject(Document):
    param = StringField()

# Fake some data, See ref: 3
for i in range(1, 6):
	to = TestObject(param=str(i))
	to.save()

# MongoengineOjbectType - needed by Graphene
class TestObjectMongoengineOjbectType(MongoengineObjectType):
    class Meta:
        model = TestObject
        interfaces = (Node,)

class Query(ObjectType):
    status = String(description='Check graphql service status')
    all_test_objects = MongoengineConnectionField(TestObjectMongoengineOjbectType)

    def resolve_status(self, args):
        return 'OK'

view_func = GraphQLView.as_view('graphql', schema=Schema(query=Query), graphiql=True)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=view_func)

@app.route('/')
def index():
    return 'Hello!'

if __name__ == '__main__':
    app.run(debug=True)
