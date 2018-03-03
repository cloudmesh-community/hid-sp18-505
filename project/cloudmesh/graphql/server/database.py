from mongoengine import connect
from models import Raingage

# connect('ccproject', host='mongomock://localhost', alias='default')
connect('ccproject', host='project_ccmongo_1', port=27017, alias='default')

def init_db():
    for i in range(1, 150):
        rg = Raingage(name='rg{}'.format(i), code='code{}'.format(i))
        rg.save()
