#image processing with opencv
import cv2
img = cv2.imread('image.jfif',1)

"""each pixel is denoted by 3 values
   RGB (which is standard),
   but in OpenCV, the standard pixel ir denoted in a BGR form"""

"""pixel colour strengths
   ranges from 0 to 255
   which means 0 is when the colour is not present at all
   and 255 means the colour has maximum presence"""

"""[0,0,0] denotes a black pixel
   and [255,255,255] denotes a white pixel"""

#returns a 3-D array
print(img.shape)
