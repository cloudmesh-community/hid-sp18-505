# File: app.py
from flask import Flask
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView

class Query(ObjectType):
    status = String(description='Check graphql service status')
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
