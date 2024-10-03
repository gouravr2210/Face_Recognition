# Face_Recognition

Project Overview
This project is a face recognition system built using OpenCV, LBPH (Local Binary Patterns Histograms) face recognizer, and Python. The system detects faces from images, trains the model using labeled face data, and predicts the identity of a person from test images.

Features
Detects faces using Haar Cascade from OpenCV.
Uses LBPH for face recognition.
Supports adding multiple subjects for training and testing.
Displays the recognized face with a bounding box and subject name.

Prerequisites
Python 3.x
OpenCV
NumPy

Project Structure
training-data/: Directory containing labeled training images in folders named s1, s2, etc.
test-data/: Directory with test images for prediction.

Main script: Contains the code for training and testing the face recognition model.

How It Works
Training:
Images from the training-data folder are loaded and converted to grayscale.
The faces are detected, cropped, and used to train the LBPH face recognizer.

Prediction:
The system predicts the identity of the person in the test image and displays the result with a bounding box and label.

Usage
Place training images in the training-data/ folder.
Place test images in the test-data/ folder.
Run the script to train the model and predict the identities in test images.

Future Improvements
Add support for live webcam face recognition.
Implement a GUI for easier interaction.
