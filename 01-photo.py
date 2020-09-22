import cv2 as cv
print("package imported")

img = cv.imread("resources/testSubject.jpeg")

cv.imshow("Output",img)
cv.waitKey(0)