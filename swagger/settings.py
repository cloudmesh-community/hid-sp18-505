from models import *

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DBNAME = 'everestdb'

# DOMAIN = {}

RESOURCE_METHODS = ['GET', 'POST']

RENDERERS = [
    'eve.render.JSONRenderer',
    'eve.render.XMLRenderer'
]