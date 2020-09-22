import cv2 as cv

faceCascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
img = cv.imread("resources/testSubject.jpeg")
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgcpy = img.copy()

faces = faceCascade.detectMultiScale(imgGray,1.1,4)     #(src,scale,min_neighbour)

for (x,y,w,h) in faces:
    cv.rectangle(imgcpy,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow("Output",imgcpy)
cv.waitKey(0)