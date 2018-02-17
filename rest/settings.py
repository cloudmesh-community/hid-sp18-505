MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DBNAME = 'everestdb'

DOMAIN = {}

# DOMAIN = {
#     'student': {
#         'schema': {
#             'firstname': {
#                 'type': 'string'
#             },
#             'lastname': {
#                 'type': 'string'
#             },
#             'school': {
#                 'type': 'string'
#             },
#             'university': {
#                 'type': 'string'
#             },
#             'email': {
#                 'type': 'string',
#                 'unique': True
#             }
#         }
#     }
# }

RESOURCE_METHODS = ['GET', 'POST']

RENDERERS = [
    'eve.render.JSONRenderer',
    'eve.render.XMLRenderer'
]