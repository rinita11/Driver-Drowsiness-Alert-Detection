import cv2
import dlib
import os
import numpy as np
from scipy.spatial import distance

# Path for model file
current_path = os.path.dirname(__file__)
model_path = os.path.join(current_path, "SVMclassifier.dat")

# Load detectors
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model_path)

# Thresholds
EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.75
FRAME_LIMIT = 15

counter = 0

# Eye Aspect Ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Mouth Aspect Ratio
def mouth_aspect_ratio(mouth):
    A = distance.euclidean(mouth[13], mouth[19])
    B = distance.euclidean(mouth[14], mouth[18])
    C = distance.euclidean(mouth[15], mouth[17])
    D = distance.euclidean(mouth[12], mouth[16])
    return (A + B + C) / (2.0 * D)

def detect_drowsiness(frame):
    global counter

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    status = "No Face"
    ear_value = 0
    mar_value = 0

    for face in faces:
        # Face rectangle
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 1)

        shape = predictor(gray, face)
        points = [(shape.part(i).x, shape.part(i).y) for i in range(68)]

        left_eye = np.array(points[36:42])
        right_eye = np.array(points[42:48])
        mouth = np.array(points[48:68])

        # Draw thin green outlines
        cv2.polylines(frame, [left_eye], True, (0,255,0), 1)
        cv2.polylines(frame, [right_eye], True, (0,255,0), 1)
        cv2.polylines(frame, [mouth], True, (0,255,0), 1)

        # Calculate EAR & MAR
        leftEAR = eye_aspect_ratio(left_eye)
        rightEAR = eye_aspect_ratio(right_eye)
        ear = (leftEAR + rightEAR) / 2.0
        mar = mouth_aspect_ratio(mouth)

        ear_value = round(ear, 3)
        mar_value = round(mar, 3)

        # Drowsiness detection
        if ear < EAR_THRESHOLD:
            counter += 1
            status = "DROWSY" if counter >= FRAME_LIMIT else "Eyes Closing"
        else:
            counter = 0
            status = "Eyes Open"

        # Display values on frame
        cv2.putText(frame, f"EAR:{ear_value}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)
        cv2.putText(frame, f"MAR:{mar_value}", (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)
        cv2.putText(frame, status, (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

    return frame, status, ear_value, mar_value