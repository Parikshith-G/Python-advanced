import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
cap=cv2.VideoCapture(0)
pTime=0
detector=htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

v_range=volume.GetVolumeRange()
print(volume.GetVolumeRange())
volume.SetMasterVolumeLevel(0, None)
#range-0=-96
v_min=v_range[1]
v_max=v_range[0]
while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if lmList:
        x1,y1=lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx,cy=(x1+x2)//2,(y1+y2)//2



        cv2.circle(img,(x1,y1),15,(255,0,0),cv2.FILLED)
        cv2.circle(img, (x2, y2),15, (255, 0, 0), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,255,0),3)
        cv2.circle(img,(cx,cy),15,(0,0,0),cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        # print(length)
        vol=np.interp(length,[30,400],[v_min,v_max])
        print(vol)
        volume.SetMasterVolumeLevel(vol, None)
        if length<50:

            cv2.circle(img, (cx, cy), 15, (100, 200, 250), cv2.FILLED)
    cTime=time.time()

    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(220,0,220),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)

