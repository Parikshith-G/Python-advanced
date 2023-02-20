import cv2
import mediapipe as mp
import time
class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mphands = mp.solutions.hands  # a mediapipe product to see if hands are present
        self.hands = self.mphands.Hands(self.mode, self.maxHands, int(self.detectionCon), int(self.trackCon))

        self.mpdraw = mp.solutions.drawing_utils  # to draw points and lines on hand


    def findHands(self,img,draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(self.imgRGB)

        if self.results.multi_hand_landmarks:
            for hands1 in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img, hands1, self.mphands.HAND_CONNECTIONS) #(check image,draw points,draw lines to connect points)


        return img

    def findPosition(self,img,handNo=0,draw=True):
        lnList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]


            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                lnList.append([id, cx, cy])

                if draw:
                    cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
        return lnList



def main():
    cap = cv2.VideoCapture(0)
    # for framerate
    pTime = 0
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lnList=detector.findPosition(img)
        if lnList:
            print(lnList[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime


        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (220, 0, 220), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ =="__main__":
    main()