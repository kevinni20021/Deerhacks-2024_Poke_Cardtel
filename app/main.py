from flask import *
import requests
import os
import base64
from preprocessor import getPhoto

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET', 'DELETE', 'PUT'])
def handle():
    if request.method == "POST":
        image_64_decode = base64.b64decode(request.json['Photo1'])
        image_result = open('p1.jpg', 'wb')  # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        image_64_decode = base64.b64decode(request.json['Photo2'])
        image_result = open('p2.jpg', 'wb')  # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        getPhoto("p1.jpg")
        getPhoto("p2.jpg")
        return "ok", 200


if __name__ == "__main__":
    app.run(host='100.112.28.221', port = 5000, debug=True)