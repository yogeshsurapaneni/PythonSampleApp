from flask import Flask, render_template, request, make_response, g
import socket
import time

localtime = time.asctime( time.localtime(time.time()) )

hostname = socket.gethostname()

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def hello():

    resp = make_response(render_template(
            'index.html',
            hostname=hostname,
            datetime=localtime,
    ))
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)

