import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
cap = cv2.VideoCapture(0)
# for framerate
pTime = 0
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lnList=detector.findPosition(img,draw=False)
    if lnList:
        print(lnList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (220, 0, 220), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

