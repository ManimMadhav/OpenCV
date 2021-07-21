"""this code will turn on your camera
   press 't' on your keyboard to terminate the window
   else it will reappear every 1 millisecond"""


import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    check, frame = capture.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('t'):
        break

capture.release()
cv2.destroyAllWindows()
