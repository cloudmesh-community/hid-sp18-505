from eve import Eve
from flask import json, Response
import platform, psutil

app = Eve()

@app.route('/status', methods=['GET'])
def status():
    """ Endpoint that returns a status message. """
    data = {
        'status': 'OK'
    }

    packet = json.dumps(data)
    resp = Response(packet, status=200, mimetype='application/json')

    return (resp)

@app.route('/sysinfo', methods=['GET'])
def processor():
    """ Returns system information. """

    data = {
        'system': platform.system(),
        'processor': platform.processor(),
        'cpu_count': psutil.cpu_count(),
        'machine': platform.machine(),
        'virtual_mem': psutil.virtual_memory().total,
        'virtual_mem_gb': psutil.virtual_memory().total / (1024.0 ** 3),
    }

    packet = json.dumps(data)
    resp = Response(packet, status=200, mimetype='application/json')

    return (resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
