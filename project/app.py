from flask import Flask
from flask_graphql import GraphQLView
from database import init_db
from schema import schema

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

default_query = '''
{
  allRaingages {
    edges {
      node {
        name,
        code
      }
    }
  }
}'''.strip()


@app.route('/')
def index():
    return("Welcome!")

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True)