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

"""each image is represented by 3-D arrays
   a 2px x 2px image can be represented as:
   [
   [[0,0,0],[255,255,255]]
   [[0,0,0],[255,255,255]]
   ]
   where 4 pixels exist, 2 black and 2 white"""

"""returns 3 values, [height,width,channels]
   channels is number of values that denote a pixel"""

print(img.shape)

#returns 3-D numpy darray containing all pixels of the image
"""first [] --> denotes image
   interior [] --> rows
   most interior []---> column pixel values inside each row"""
