from flask import Flask, Response, render_template
import cv2
import mediapipe as mp
import numpy as np
import functions
import os

app = Flask(__name__)

cap = cv2.VideoCapture(0)

@app.route('/')
def index():
    cap.release()
    return render_template('index.html')

@app.route('/biceps')
def show_biceps():
    cap = cv2.VideoCapture(0)
    return Response(functions.biceps(cap),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/przysiad')
def show_przysiad():
    cap = cv2.VideoCapture(0)
    return Response(functions.przysiad(cap),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)

