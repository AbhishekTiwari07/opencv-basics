import cv2 as cv
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    shape = "unknown"
    contours,heirarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>100:
            cv.drawContours(imgBlank,cnt,-1,(255,0,0),3)      #drawContour(outputSrc,cnt,limit,BRG,Thickness)
            peri = cv.arcLength(cnt,True)                       #arcLength(cnt,ClosedOrNot)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)        #gives corner of points
            vertices = len(approx)
            x,y,width,height = cv.boundingRect(approx)

            if(vertices == 3):
                shape = "Triangle"
            elif vertices == 4:
                if width/float(height) > 0.95 and width/float(height) < 1.05:
                    shape = "Square"
                else:
                    shape = "Rectangle"
            elif vertices == 5:
                shape = "Pentagan"  
            elif vertices == 6:
                shape = "Hexagon"

            cv.rectangle(imgContour,(x,y),(x+width,y+height),(0,255,255),2)
            cv.putText(imgContour,shape,(x+int(width/2)-70,y+int(height/2)),cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
            
            


path = "resources/shapes.jpg"
img = cv.imread(path)
imgContour = img.copy()
#img = cv.resize(cv.imread(path),(512,400))

imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(7,7),2)
imgCanny = cv.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)

imgStack = stackImages(0.3,([img,imgGray,imgBlur],[imgCanny,imgContour,imgBlank]))

cv.imshow("Stacked Images",imgStack)
cv.waitKey(0)