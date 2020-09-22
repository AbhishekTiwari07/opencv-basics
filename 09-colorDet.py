import cv2 as cv
import numpy as np

def empty(a):
    pass

path = "resources/cars.jpg"

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",(640,300))
cv.createTrackbar("Hue min","TrackBars",0,179,empty)         #createTrackbar(" ","window-Name",initialValue,endValue)
cv.createTrackbar("Hue max","TrackBars",7,179,empty)
cv.createTrackbar("Sat min","TrackBars",107,255,empty)
cv.createTrackbar("Sat max","TrackBars",255,255,empty)
cv.createTrackbar("Val min","TrackBars",72,255,empty)
cv.createTrackbar("Val max","TrackBars",255,255,empty)

img = cv.imread(path)
img = cv.resize(img,(400,600))
imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)

while True:
    output = cv.resize(imgHSV,(400,600))
    h_min = cv.getTrackbarPos("Hue min","TrackBars")
    h_max = cv.getTrackbarPos("Hue max","TrackBars")
    s_min = cv.getTrackbarPos("Sat min","TrackBars")
    s_max = cv.getTrackbarPos("Sat max","TrackBars")
    v_min = cv.getTrackbarPos("Val min","TrackBars")
    v_max = cv.getTrackbarPos("Val max","TrackBars")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv.inRange(output,lower,upper)

    imgResult = cv.bitwise_and(img,img,mask=mask)

    cv.imshow("Original",img)
    #cv.imshow("HSV",output)
    cv.imshow("Mask",mask)
    cv.imshow("Result",imgResult)
    if ( cv.waitKey(1) & 0xFF == ord('q') ):
        break