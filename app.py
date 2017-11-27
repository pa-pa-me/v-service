from flask import Flask, request
from redis import Redis, RedisError
import os
import socket
import facemorpher
import tempfile
from common.image_helper import save_base64_image_to_tmp

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

@app.route("/face/average", methods=['POST'])
def face_average():
    json = request.get_json(silent=True)

    temp_me = save_base64_image_to_tmp(json['me'])
    temp_you = save_base64_image_to_tmp(json['you'])

    with tempfile.NamedTemporaryFile(dir='/tmp', delete=False) as tmpFile:
        temp_file_name = tmpFile.name

    facemorpher.averager([temp_me, temp_you], out_filename=temp_file_name)

    return temp_file_name

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8880)
