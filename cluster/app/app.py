import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    c = get_container()    
    return jsonify({'container': c})

def get_container():
    """
    Full acknowledgement to https://github.com/monicagangwar for example code in 
    docker-swarm-vagrant repo.
    """
    container = None
    statement = ['cat','/proc/self/cgroup']
    p = subprocess.Popen(statement, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    if out:
        out = str(out)
        container = out.split("\n")[0].split('/')[-1]

    return container[:-3]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
