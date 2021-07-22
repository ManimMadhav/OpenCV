import cv2
import mediapipe as mp

img = cv2.imread("hands.jfif")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#print( img )

#cv2.imshow("Two Hands", img)
#cv2.waitKey()

mpHands = mp.solutions.hands

hands = mpHands.Hands()

results = hands.process(imgRGB)

print(results)
print(results.multi_hand_landmarks) # 42 for 2 hands (21 points each have been identified by Google)


print(img.shape)
drawTools = mp.solutions.drawing_utils
# 2 hands therefore 2 iterations

capture = cv2.VideoCapture(0)
while True:

    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            drawTools.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)

    cv2.imshow("Video Feed:",img)

    key = cv2.waitKey(1)

    if key == 27: # escape
        break

for handlms in results.multi_hand_landmarks:
    drawTools.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)
