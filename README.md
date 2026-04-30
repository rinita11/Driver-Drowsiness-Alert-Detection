# Driver Drowsiness Alert Detection System

## Description

This project is a real-time driver drowsiness detection system that helps prevent road accidents. It uses computer vision and machine learning techniques to monitor the driver's eye movements and alert them when signs of drowsiness are detected.

## Features

* Real-time face detection
* Eye tracking using OpenCV
* Drowsiness alert system (alarm)
* Machine learning model (SVM)
* Easy-to-use interface

## Technologies Used

* Python
* OpenCV
* NumPy
* Machine Learning (SVM)

## Project Structure

Driver_Drowsiness_Project/
│
├── backend/
│   ├── main.py
│   ├── SVMclassifier.dat
│
├── frontend/
│   ├── index.html
│
├── README.md

## How It Works

1. The webcam captures the driver's face in real-time.
2. Face detection is performed using OpenCV.
3. Eye regions are extracted.
4. The SVM model classifies whether eyes are open or closed.
5. If eyes remain closed for a certain time, an alarm is triggered.

## Installation & Setup

1. Clone the repository:
   git clone https://github.com/rinita11/Driver-Drowsiness-Alert-Detection.git

2. Navigate to the project folder:
   cd Driver_Drowsiness_Project

3. Install dependencies:
   pip install -r requirements.txt

4. Run the project:
   python main.py

## Output

* Detects driver face and eyes in real time
* Alerts when drowsiness is detected

## Future Enhancements

* Mobile application integration
* Deep learning-based model
* Cloud-based monitoring

## Conclusion

This project helps in reducing road accidents by detecting driver drowsiness in real time and providing alerts.
