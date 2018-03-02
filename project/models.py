from mongoengine import Document
from mongoengine.fields import (DateTimeField, ReferenceField, StringField)

class Raingage(Document):
    meta = {'collection': 'raingage'}
    code = StringField()
    name = StringField()
