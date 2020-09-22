import cv2 as cv
import numpy as np

img = cv.imread("resources/testSubject.jpeg")
kernal = np.ones((5,5),np.uint8)

imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(img,(9,9),0)
imgCanny = cv.Canny(imgBlur,50,100)
imgDialation = cv.dilate(imgCanny,kernal,iterations = 1)
imgEroded = cv.erode(imgDialation,kernal,iterations = 1)

#cv.imshow("Gray Image",imgGray)
#cv.imshow("Blur Image",imgBlur)
cv.imshow("Canny Image",imgCanny)
cv.imshow("Dilation Image",imgDialation)
cv.imshow("Eroded Image",imgEroded)
cv.waitKey(0)