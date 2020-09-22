import cv2 as cv
import numpy as np

img = cv.imread("resources/cards.jpg")

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv.imshow("Horizontal",imgHor)
cv.imshow("Verticle",imgVer)
cv.waitKey(0)