from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from DrowsinessDetector import detect_drowsiness

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect")
def detect():
    return render_template("detect.html")

@app.route("/process_frame", methods=["POST"])
def process_frame():
    file = request.files["frame"]
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    frame, status, ear, mar = detect_drowsiness(frame)

    _, buffer = cv2.imencode(".jpg", frame)
    jpg_as_text = base64.b64encode(buffer).decode("utf-8")

    return jsonify({
        "image": jpg_as_text,
        "status": status,
        "ear": ear,
        "mar": mar
    })

if __name__ == "__main__":
    app.run(debug=True)