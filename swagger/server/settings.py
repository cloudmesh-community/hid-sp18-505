from os import environ

if environ.get('MONGO_HOST') is not None:
    MONGO_HOST = environ.get('MONGO_HOST')
else:
    MONGO_HOST = 'localhost'

MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
# MONGO_USERNAME = '<your username>'
# MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'swagger'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
# RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
# ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'raingages': {
        'schema': {
            'code': { 'type': 'string' },
            'name': { 'type': 'string' },
            'latitude': { 'type': 'number', 'format': 'double'},
            'longitude': { 'type': 'number', 'format': 'double'}
        }
    },
    'precipevents': {
        'schema': {
            'gage': {'type': 'string'},
            'year': {'type': 'number', 'format': 'integer'},
            'month': {'type': 'number', 'format': 'integer'},
            'precip': {'type': 'number', 'format': 'double'},
        }
    }
}

ENDERERS = [
    'eve.render.JSONRenderer',
    'eve.render.XMLRenderer'
]