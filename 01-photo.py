import cv2 as cv

img = cv.imread("resources/testSubject.jpeg")

cv.imshow("Output",img)
cv.waitKey(0)