import cv2
from flask import *
import requests
import numpy as np
import os
import base64
from preprocessor import getPhoto
from namelookup import name_lookup
import tensorflow as tf
import math

app = Flask(__name__)
class_names = ["Low Grade", "PSA 6", "PSA 7", "PSA 8", "PSA 9", "PSA 10"]


@app.route('/', methods=['POST'])
def handle():
    if request.method == "POST":
        image_64_decode = base64.b64decode(request.json['Photo1'])
        image_result = open('front.jpg', 'wb')  # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        image_64_decode = base64.b64decode(request.json['Photo2'])
        image_result = open('back.jpg', 'wb')  # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        f = getPhoto('front.jpg')
        cv2.imshow("front.jpg", f)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        if not f.any():
            return "retake image", 400
        f = np.expand_dims(f, axis=0)
        print(f.shape)
        new1 = model.predict(f)
        pred1 = np.argmax(new1, axis=1)
        print(pred1)
        b = getPhoto('back.jpg')
        if not b.any():
            return "retake image", 400
        b = np.expand_dims(b, axis=0)
        print(b.shape)
        new2 = model.predict(b)
        pred2 = np.argmax(new2, axis=1)
        print(pred2)
        index = math.floor((float(pred1) + 1) * 0.4 + (float(pred2) + 1) * 0.6 - 1)
        price = name_lookup(request.json['name'], index)

        response = {'grade': class_names[index], 'price': price}
        return response, 200


if __name__ == "__main__":
    model = tf.keras.models.load_model(os.path.join(os.getcwd(), '..\model\pokegrade.h5'))
    app.run(host='142.1.200.8', port=5000, debug=True)
