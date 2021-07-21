import numpy as np
import cv2

capture = cv2.VideoCapture(0)
while True:
    check, frame = capture.read()
    #width of our video frame
    width = int(capture.get(3))
    #height of our video frame
    height = int(capture.get(4))

    image = np.zeros(frame.shape, np.uint8)

    quarter_frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
    image[:height//2, :width//2] = quarter_frame
    image[height//2:, :width // 2] = quarter_frame
    image[:height//2, width // 2:] = quarter_frame
    image[height//2:,  width // 2:] = quarter_frame

    cv2.imshow('frame', image)
    
    #press 't' to terminate the video
    if cv2.waitKey(1) == ord('t'):
        break

capture.release()
cv2.destroyAllWindows()