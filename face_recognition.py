#import OpenCV module, os module, numpy
import cv2

import os

import numpy as np

subjects = ["", "Gourav", "Tom Cruise"]


def detect_face(img):
    #convert images to gray image 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier('F:\FaceRecogniton_Project(Intrenship)\opencv-files\lbpcascade_frontalface.xml')
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    if (len(faces) == 0):
        return None, None
      
    (x, y, w, h) = faces[0]
    
    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
  
    dirs = os.listdir(data_folder_path)
    
    faces = []
    
    labels = []
    
    for dir_name in dirs:
        
        if not dir_name.startswith("s"):
            continue;
            
        label = int(dir_name.replace("s", ""))
        
        subject_dir_path = data_folder_path + "/" + dir_name
        
        subject_images_names = os.listdir(subject_dir_path)
      
        for image_name in subject_images_names:
            
            if image_name.startswith("."):
                continue;
            
            image_path = subject_dir_path + "/" + image_name

            image = cv2.imread(image_path)
            
            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)
            
            face, rect = detect_face(image)
            
            if face is not None:
               
                faces.append(face)
                
                labels.append(label)
            
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return faces, labels

print("Preparing data...")
faces, labels = prepare_training_data("training-data")
print("Data prepared")

print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

#create LBPH face recognizer 
face_recognizer = cv2.face.LBPHFaceRecognizer_create()


#we can use EigenFaceRecognizer, FisherFaceRecognizer by replacing above line with 
#face_recognizer = cv2.face.EigenFaceRecognizer_create()

#face_recognizer = cv2.face.FisherFaceRecognizer_create()

#train the face recognizer of our training faces
face_recognizer.train(faces, np.array(labels))

#function to draw rectangle on image 

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#function to draw text on give image starting from

def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

#this function recognizes the person in image passed and draws a rectangle around detected face with name of the subject

def predict(test_img):
    
    img = test_img.copy()
    #detect face from the image
    face, rect = detect_face(img)

    #predict the image using our face recognizer 
    label, confidence = face_recognizer.predict(face)
    #get name of respective label returned by face recognizer
    label_text = subjects[label]
    
    #draw a rectangle around face detected
    draw_rectangle(img, rect)
    #draw name of predicted person
    draw_text(img, label_text, rect[0], rect[1]-5)
    
    return img

print("Predicting images...")

#load test images
test_img1 = cv2.imread("F:\FaceRecogniton_Project(Intrenship)\test-data\test1.jpg")
test_img2 = cv2.imread("F:F:\FaceRecogniton_Project(Intrenship)\test-data\test2.jpg")

#perform a prediction
predicted_img1 = predict(test_img1)
predicted_img2 = predict(test_img2)

print("Prediction complete")

#display both images
cv2.imshow(subjects[1], cv2.resize(predicted_img1, (400, 500)))
cv2.imshow(subjects[2], cv2.resize(predicted_img2, (400, 500)))
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()