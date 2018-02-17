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


@app.route('/api/v1/performance/<string:attribute>', methods=['GET'])
def performance(attribute):
    """ A little smater routing system.
    """

    data = None

    if attribute == 'system':
        data = { 'system': platform.system() }
    elif attribute == 'processor':
        data = { 'processor': platform.processor() }
    elif attribute in ['cpu_count', 'cpucount'] :
        data = { 'cpu_count': psutil.cpu_count() }
    elif attribute == 'machine':
        data = { 'machine': platform.machine() }
    elif attribute in ['virtual_mem', 'virtualmem']:
        data = { 'virtual_mem': psutil.virtual_memory().total }
    elif attribute in ['virtual_mem_gb', 'virtualmemgb']:
        data = { 'virtual_mem_gb': psutil.virtual_memory().total / (1024.0 ** 3) }
    elif attribute == 'all':
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

    return(resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
