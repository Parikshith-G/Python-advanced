import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands # a mediapipe product to see if hands are present
hands = mphands.Hands()
mpdraw=mp.solutions.drawing_utils # to draw points and lines on hand
#for framerate
pTime=0
cTime=0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hands1 in results.multi_hand_landmarks:
            for id,lm in enumerate(hands1.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),(lm.y*h)
                print(id, cx,cy)
            mpdraw.draw_landmarks(img, hands1, mphands.HAND_CONNECTIONS) #(check image,draw points,draw lines to connect points)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(220,0,220),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


