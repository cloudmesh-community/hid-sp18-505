from eve import Eve
from flask import json, Response

app = Eve()

@app.route('/status', methods=['GET'])
def status():
    """ Endpoint that returns a status message. """
    data = {
        'status': 'OK'
    }

    packet = json.dumps(data)

    resp = Response(packet, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

