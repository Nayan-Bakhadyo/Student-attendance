import numpy as np
import cv2
import os

import face_recognition as fr 
#print(fr)

test_img=cv2.imread(r'C:\Users\times\Desktop\Face Recognition\test img\img2.jpg')

faces_detected,gray_img=fr.faceDetection(test_img)
print("Face detected: ",faces_detected)

#Training will begin from here

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\times\Desktop\Face Recognition\trainingData.yml')

name={0: 'Saugat',1: 'Safal'}

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+w,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print(label)
    print(confidence)
    fr.draw_rect(test_img,face)
    predict_name=name[label]
    if(confidence>52):
        fr.put_text(test_img,'unknown',x,y)
    else: 
        fr.put_text(test_img,predict_name,x,y)

resized_img=cv2.resize(test_img,(1000,700))

cv2.imshow("face detection ",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()