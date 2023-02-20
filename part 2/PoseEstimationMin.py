import cv2
import mediapipe as mp

cap=cv2.VideoCapture("Pose Videos/(1).mp4")
cap.set(3,1000)
cap.set(4,100)
while True:
    success,img=cap.read()
    cv2.imshow("Image",img)
    cv2.waitKey(100)