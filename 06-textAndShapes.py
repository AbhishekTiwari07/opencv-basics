import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[:] = 0,255,0

#cv.line(img,(0,0),(300,300),(0,0,255),3)    #(src,initial_coordinate,end_coordinate,color(bgr),thickness)
cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

cv.rectangle(img,(50,50),(250,350),(120,210,50),2)      # to fill rectangle use (img,begin,end,color,cv.FILLED)

cv.circle(img,(256,256),100,(255,255,50),5)

cv.putText(img," Edit text ", (400,450),cv.FONT_HERSHEY_COMPLEX,0.5,(200,100,200),2)

cv.imshow("Image",img)
cv.waitKey(0)