from eve import Eve
from flask import json, Response
import platform, psutil

app = Eve()

@app.route('/api/v1.0/status', methods=['GET'])
def status():
    """ Endpoint that returns a status message. """

    data = {'status': 'OK'}

    packet = json.dumps(data)
    resp = Response(packet, status=200, mimetype='application/json')

    return (resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
