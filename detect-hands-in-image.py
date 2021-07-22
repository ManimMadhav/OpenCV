#detecting hands with mediapipe

import cv2
import mediapipe as mp

img = cv2.imread("hands.jfif",-1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
drawTools = mp.solutions.drawing_utils
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
results = hands.process(imgRGB)


for handlms in results.multi_hand_landmarks:
    drawTools.draw_landmarks(img,handlms, mpHands.HAND_CONNECTIONS)
