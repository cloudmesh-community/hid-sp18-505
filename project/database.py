from mongoengine import connect
from models import Raingage

connect('ccproject', host='mongomock://localhost', alias='default')

def init_db():
    for i in range(1, 15000):
        rg = Raingage(name='rg{}'.format(i), code='code{}'.format(i))
        rg.save()
