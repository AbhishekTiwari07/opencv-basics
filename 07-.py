import cv2 as cv
import numpy as np

img = cv.imread("resources/cards.jpg")

width,height = 250,350
pts1 = np.float32([[223,88],[432,135],[370,429],[160,382]])         #[x,y]
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgOutput = cv.warpPerspective(img,matrix,(width,height))

cv.imshow("Output",img)
cv.imshow("Output2",imgOutput)
cv.waitKey(0)