import cv2 as cv

img = cv.imread("resources/testSubject.jpeg")
print(img.shape)

imgResize = cv.resize(img,(400,600))
print(imgResize.shape)

imgCrop = img[0:500,150:450]

#cv.imshow("Output",img)
cv.imshow("Output2",imgResize)
cv.imshow("Output3",imgCrop)
cv.waitKey(0)