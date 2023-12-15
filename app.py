import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from tensorflow import keras
from keras.models import load_model
import numpy as np
from PIL import Image
from google.cloud import storage

app = Flask(__name__)
app.config["ALLOWED_EXTENSIONS"] = set(['png', 'jpg', 'jpeg'])
# app.config["UPLOAD_FOLDER"] = "static/uploads"

def allowed_file(filename):
    return "." in filename and \
        filename.split(".", 1)[1] in app.config["ALLOWED_EXTENSIONS"]

model = load_model("model.h5", compile=False)
with open("labels.txt", "r") as file:
    labels = file.read().splitlines()

@app.route("/")
def index():
    return jsonify({
        "status": {
            "code": 200,
            "message": "Success fetching the API",
        },
        "data": None
    }), 200

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        image = request.files["image"]
        if image and allowed_file(image.filename):
            # Save Input Image
            filename = secure_filename(image.filename)
            # image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            # image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            bucket_name = 'testmllll'
            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(filename)
            blob.upload_from_string(image.read(), content_type=image.content_type)


            #Pre-Processing input image
            img = Image.open(image).convert("RGB")
            img = img.resize((150, 150))
            img_array = np.asarray(img)
            img_array = np.expand_dims(img_array, axis=0)
            normalized_image_array = (img_array.astype(np.float32) / 127.5) - 1
            data = np.ndarray(shape=(1, 150, 150, 3), dtype=np.float32)
            data[0] = normalized_image_array

            # Predicting the image
            prediction = model.predict(data)
            index = np.argmax(prediction)
            class_names = labels[index]
            confidence_score = prediction[0][index]

            #redirect
            external_api_url = 'https://project-bangkit-fgymidl6bq-uc.a.run.app/getExerciseByEquipment?equipment='+class_names[2:]
            response = requests.get(external_api_url)
            hasil_request = response.json()

            return jsonify({
                "status": {
                    "code": 200,
                    "message": "Success Predicting",
                },
                "data": {
                    "gym_equipment_prediction": class_names[2:],
                    "confidence": float(confidence_score),
                    "exercise": hasil_request
                }
            }), 200
        else:
            return jsonify({
                "status" : {
                    "code": 400,
                    "message": "Client side error"
                },
                "data": None
            }), 400
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed"
            },
            "data": None
        }), 405



if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=8080)