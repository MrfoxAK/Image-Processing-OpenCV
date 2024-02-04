import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)


while True:
     success, img = cap.read()
     hands, img = detector.findHands(img)
    
     if hands:
          # Get landmarks of the first hand (assuming only one hand is present)
          lmList = hands[0]["lmList"]
          bboxInfo = hands[0]["bbox"]

          # Do something with lmList and bboxInfo
          print(lmList, bboxInfo)


     cv2.imshow("Image", img)
     cv2.waitKey(1)



























