from flask import *
import requests
import os
import base64
from preprocessor import getPhoto
from namelookup import name_lookup

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET', 'DELETE', 'PUT'])
def handle():
    if request.method == "POST":
        image_64_decode = base64.b64decode(request.json['Photo1'])
        image_result = open('front.jpg', 'wb')  # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        image_64_decode = base64.b64decode(request.json['Photo2'])
        image_result = open('back.jpg', 'wb')  # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        getPhoto('front.jpg')
        getPhoto('back.jpg')
        price = name_lookup(request.json['name'], 9)
        response = {'grade' : 9, 'price':price}
        return response, 200


if __name__ == "__main__":
    app.run(host='100.112.28.221', port = 5000, debug=True)