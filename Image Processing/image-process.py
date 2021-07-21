#image processing with opencv
import cv2
import random
img = cv2.imread('image.jfif',-1)

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
print(img.shape)

"""first [] --> denotes image
   interior [] --> rows
   most interior []---> column pixel values inside each row"""

"""returns 3 values, [height,width,channels]
   channels is number of values that denote a pixel"""


#changing pixel colours
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




#superimpose two images
img2 = cv2.imread("myafce.jpg",-1)

#in opencv the area on which image is to be superimposed must be = dimensions of image being superimposed
img[5:168,230:417] = img2
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
