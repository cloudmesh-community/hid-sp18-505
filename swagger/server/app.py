from eve import Eve
from flask import json, Response, render_template
import platform, psutil
from eve_swagger import swagger, add_documentation
from pymongo import MongoClient

app = Eve(__name__, template_folder='templates')
app.register_blueprint(swagger)

mongo_client = MongoClient('127.0.0.1', 27017)
mongo_db = mongo_client.swagger

app.config['SWAGGER_INFO'] = {
    'title': 'Swagger API',
    'version': '1.0',
    'description': 'API Description',
    'termsOfService': '',
    'contact': {
        'name': 'acatejr',
        'url': 'http://127.0.0.1'
    },
    'license': {
        'name': 'MIT',
        'url': 'http://127.0.0.1',
    },
    'schemes': ['http', 'https'],
}

@app.route('/status')
def status():
    """ Endpoint that returns a status message. """
    data = {
        'status': 'OK'
    }

    packet = json.dumps(data)
    resp = Response(packet, status=200, mimetype='application/json')

    return (resp)

@app.route('/raingages')
def raingages():
    data = {}
    raingages = mongo_db.raingages
    data = raingages.find()
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return (resp)

@app.route('/precipevents')
def precipevents():
    data = {}
    precipevents = mongo_db.precipevents
    data - precipevents.find()
    print("Here")
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return (resp)

@app.route('/apidocs')
def apidocs():
    return render_template('swaggerui/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
